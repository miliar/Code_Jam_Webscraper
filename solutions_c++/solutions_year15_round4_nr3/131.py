#include <cassert>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>

struct Edge
{
	Edge(int uu, int vv) : u(uu), v(vv), flow(0) {}

	int u, v, flow;
};


bool bfs(const int s, const int t, const std::vector< std::vector<Edge *> > & dir, const std::vector< std::vector<Edge *> > & rev, const int n)
{
	std::vector<int> delta(n, 0);
	std::vector<Edge *> incoming(n, nullptr);
	std::queue<int> q;
	
	q.push(s);
	
	while(!q.empty())
	{
		int u = q.front();
		q.pop();
		
		if(u == t)
		{
			for(int u = t; u != s; )
			{
				Edge & e = *incoming[u];
				e.flow += delta[u];
				u = (delta[u] == 1) ? e.u : e.v;
			}
			
			return true;
		}
		
		for(int i = 0; i < (int)dir[u].size(); i++)
		{
			Edge & e = *dir[u][i];
			if(e.flow < 1 && incoming[e.v] == 0)
			{
				incoming[e.v] = &e;
				delta[e.v] = 1;
				q.push(e.v);
			}
		}
		
		for(int i = 0; i < (int)rev[u].size(); i++)
		{
			Edge & e = *rev[u][i];
			if(e.flow > 0 && incoming[e.u] == 0)
			{
				incoming[e.u] = &e;
				delta[e.u] = -1;
				q.push(e.u);
			}
		}
	}
	
	return false;
}

int solve(const std::vector< std::vector<int> > & v, const int words)
{
	const int n = (int)v.size();
	std::vector< std::vector<Edge *> > dir(n + 2 * words, std::vector<Edge *>());
	std::vector< std::vector<Edge *> > rev(n + 2 * words, std::vector<Edge *>());

	for(int i = 0; i < (int)v.size(); i++)
		for(int j = 0; j < (int)v[i].size(); j++)
		{
			int w = v[i][j];
			
			Edge * d = new Edge(i, n + w);
			dir[i].push_back(d);
			rev[n + w].push_back(d);
			
			Edge * r = new Edge(n + words + w, i);
			dir[n + words + w].push_back(r);
			rev[i].push_back(r);
		}
		
	for(int i = 1; i < words; i++)
	{
		Edge * e = new Edge(n + i, n + words + i);
		dir[n + i].push_back(e);
		rev[n + words + i].push_back(e);
	}
	
	int flow = 0;
	while(bfs(0, 1, dir, rev, n + 2 * words))
		flow++;
	return flow;
}

char buf[1000000];

int main()
{
	freopen("input.txt", "r", stdin);
	
	int tn;
	scanf("%i\n", &tn);
	for(int t = 1; t <= tn; t++)
	{
		int n;
		scanf("%i\n", &n);
		
		std::map<std::string, int> s;
		int free = 1;
		std::vector< std::vector<int> > v;
		
		for(int line = 0; line < n; line++)
		{
			std::vector<int> ln;
			
			gets(buf);
			for(int i = 0; buf[i] != '\0'; )
			{
				std::string c;
				while(std::isalpha(buf[i]))
					c += buf[i++];
					
				if(c.length() > 0)
				{
					//printf("%s\n", c.c_str());
					if(s[c] == 0)
						s[c] = free++;
					ln.push_back(s[c]);
				}
				
				if(buf[i] != '\0')
					i++;
			}
			
			std::sort(ln.begin(), ln.end());
			v.push_back(ln);
		}


		printf("Case #%i: %i\n", t, solve(v, free));
	}
	
	return 0;
}

