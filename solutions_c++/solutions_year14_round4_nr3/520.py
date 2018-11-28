#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

/*
int main()
{
	ifstream cin;
	cin.open("in.in");
	ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i =1; i <=t; i++)
	{
		int n,l;
		cin>>n>>l;
		vector<string> sw(n);
		vector<string> d(n);
		for (int j = 0; j < n; j++) cin>>sw[j];
		for (int j = 0; j < n; j++) cin>>d[j];
		sort(d.begin(), d.end());
		int mn = 1000000;
		for (int k = 0; k < n; k++)
		{
			int ch = 0;
			vector<bool> tk(l, false);
			for (int z = 0; z<l; z++)
			{
				if (sw[k][z] != d[0][z])
				{
					ch++;
					tk[z] = true;
				}
			}
			vector<string> sw2 = sw;
			for (int a = 0; a < n; a++)
			{
				for (int z = 0; z<l; z++)
				{
					if (sw2[a][z] == '0' && tk[z]) sw2[a][z] = '1';
					else if (sw2[a][z] == '1' && tk[z]) sw2[a][z] = '0';
				}
			}
			sort(sw2.begin(), sw2.end());
			bool ok = true;
			//cout<<ch<<endl;
			for (int a = 0; a < n; a++)
			{
				if (d[a] != sw2[a]) ok =false;
			}
			if (ok)
				mn = min(mn, ch);
		}
		if (mn == 1000000)
		{
			cout<<"Case #"<<i<<": NOT POSSIBLE"<<endl;
		}
		else
			cout<<"Case #"<<i<<": "<<mn<<endl;
	}
}


int sz[1005];
int dp[1005];
vector<vector<int> > tr;
int dfs1(int i, int p)
{
	int r = 1;
	for (int j = 0; j < tr[i].size(); j++)
	{
		if (tr[i][j] != p)
			r+= dfs1(tr[i][j], i);
	}
	return sz[i] = r;
}

int sol(int i , int p)
{
	if (dp[i] != -1) return dp[i];
	int ch = tr[i].size();
	int tot = 0;
	for (int j=0; j < tr[i].size(); j++) if (tr[i][j] != p) tot += sz[tr[i][j]];
	if (p != -1) ch--;
	if (ch == 0) return 0;
	if (ch == 1)
	{
		for (int j = 0; j < tr[i].size(); j++)
		{
			if (tr[i][j] != p)
				return dp[i] = sz[tr[i][j]];
		}
	}
	else
	{
		int mn = 1000000000;
		vector<int> mns;
		for (int j = 0; j < tr[i].size(); j++)
		{
			if (tr[i][j] == p) continue;
			mns.push_back(sol(tr[i][j], i) - sz[tr[i][j]]);
		}
		sort(mns.begin(), mns.end());
		return dp[i] = tot+mns[0]+mns[1];
	}
}

int main()
{
	ifstream cin;
	cin.open("in.in");
	ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i =1; i <=t; i++)
	{
		int n;
		cin>>n;
		tr = vector<vector<int> >(n);
		for(int j = 0; j < n-1; j++)
		{
			int a,b;
			cin>>a>>b;
			tr[a-1].push_back(b-1);
			tr[b-1].push_back(a-1);
		}
		int mn = 10000;
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < 1005; k++)
				sz[k] = 0,dp[k] = -1;
			dfs1(j,-1);
			mn = min(sol(j,-1), mn);
		}
		cout<<"Case #"<<i<<": "<<mn<<endl;
	}
}


int main()
{
	ifstream cin;
	cin.open("in.in");
		ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	int c[701] = {0};
	for (int i = 1; i <= t; i++)
	{
		for (int j = 0; j < 701; j++) c[j] = 0;
		int n, x;
		cin>>n>>x;
		for (int j = 0; j < n; j++)
		{
			int a;
			cin>>a;
			c[a]++;
		}
		int res = 0;
		int y = 700;
		for (int j = 1; j <=700; j++)
		{
			while (c[j] > 0)
			{
				y = min(y, x-j);
				c[j]--;
				res++;
				while (c[y] == 0 && y >=0) y--;
				if (y >=0)
				{
					c[y]--;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
}


int main()
{
	ifstream cin;
	cin.open("in.in");
		ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin>>n;
		int mx = 0;
		vector<int> a(n);
		for (int j=0; j < n; j++)
		{
			cin>>a[j];
			if (a[j] > a[mx]) mx = j;
		}
		int mn = 100000;
		for (int k = 0; k < (1<<n); k++)
		{
			int cnt = 0;
			vector<pair<int,int> > bef, aft;
			for (int j = 0; j < n; j++)
			{
				if (j == mx) continue;
				if ((k&(1<<j)) > 0) aft.push_back(make_pair(a[j], j));
				else bef.push_back(make_pair(a[j], j));
			}
			sort(bef.begin(), bef.end());
			sort(aft.begin(), aft.end());
			reverse(aft.begin(), aft.end());
			vector<int> r;
			for (int j = 0; j< bef.size(); j++) r.push_back(bef[j].second);
			r.push_back(mx);
			for (int j = 0; j< aft.size(); j++) r.push_back(aft[j].second);
			vector<int> aa(n,0);
			
			for (int j = 0; j < n; j++)
			{
				for (int z = j+1; z < n; z++)
					if (r[z] < r[j]) cnt++;
			}
			mn = min(cnt, mn);
		}
		cout<<"Case #"<<i+1<<": "<<mn<<endl;
	}
}


int main()
{
	ifstream cin;
	cin.open("in.in");
		ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin>>n;
		int mx = 0;
		vector<pair<int,int> > a(n);
		for (int j=0; j < n; j++)
		{
			cin>>a[j].first;
			a[j].second = j;
			if (a[j].first > a[mx].first) mx = j;
		}
		sort(a.begin(), a.end());
		int cnt = 0;
		for (int j = 0; j < n; j++)
		{
			int bef = 0;
			int aft = 0;
			for (int k = j+1; k < n;k++)
			{
				if (a[k].second < a[j].second) bef++;
				else aft++;
			}
			cnt += min(bef, aft);
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
}


int mx = 0;
int n,m;
vector<string> a;
vector<int> ch;
int cnt = 0;
void prm(int i)
{
	if (i == m)
	{
		vector<set<string> >pr(n);
		for (int j = 0; j < m; j++)
		{
			string s = "";
			for (int k = 0; k <= a[j].size(); k++)
			{
				pr[ch[j]].insert(s);
				if (k < a[j].size()) s+=a[j][k];
			}
		}
		int sm = 0;
		for (int j = 0; j < n; j++) sm += pr[j].size();
		if (sm > mx)
		{
			mx = sm;
			cnt = 1;
		}
		else if (sm == mx) cnt++;
	}
	else
	{
		for (int j = 0; j < n; j++)
		{
			ch[i] = j;
			prm(i+1);
		}
	}
}

int main()
{
	ifstream cin;
	cin.open("in.in");
		ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		cin>>m>>n;
		a = vector<string> (m);
		mx =0;
		cnt = 0;
		ch = vector<int> (m);
		for (int j = 0; j < m; j++) cin>>a[j];
		prm(0);
		cout<<"Case #"<<i<<": "<<mx<<" "<<cnt<<endl;
	}
}
*/

const int INF = 2000000000;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct Dinic {
  int N;
  vector<vector<Edge> > G;
  vector<Edge *> dad;
  vector<int> Q;
  
  Dinic(int N) : N(N), G(N), dad(N), Q(N) {}
  
  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  long long BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), (Edge *) NULL);
    dad[s] = &G[0][0] - 1;
    
    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < G[x].size(); i++) {
	Edge &e = G[x][i];
	if (!dad[e.to] && e.cap - e.flow > 0) {
	  dad[e.to] = &G[x][i];
	  Q[tail++] = e.to;
	}
      }
    }
    if (!dad[t]) return 0;

    long long totflow = 0;
    for (int i = 0; i < G[t].size(); i++) {
      Edge *start = &G[G[t][i].to][G[t][i].index];
      int amt = INF;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	if (!e) { amt = 0; break; }
	amt = min(amt, e->cap - e->flow);
      }
      if (amt == 0) continue;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	e->flow += amt;
	G[e->to][e->index].flow -= amt;
      }
      totflow += amt;
    }
    return totflow;
  }

  long long GetMaxFlow(int s, int t) {
    long long totflow = 0;
    while (long long flow = BlockingFlow(s, t))
      totflow += flow;
    return totflow;
  }
};


int main()
{
	ifstream cin;
	cin.open("in.in");
	ofstream cout;
	cout.open("out.out");
	int t;
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		int w,h,b;
		cin>>w>>h>>b;
		vector<string> mat(w, string(h,'.'));
		for (int j = 0; j < b; j++)
		{
			int x0,y0,x1,y1;
			cin>>x0>>y0>>x1>>y1;
			for (int a = x0; a<= x1; a++) for (int b = y0; b<= y1; b++)
				mat[a][b] = 'x';
		}
		Dinic g(2*(w*h)+2);
		for (int a = 0; a < w; a++) for (int b = 0; b < h; b++) g.AddEdge(a*h+b, w*h + a*h+b, 1);
		for (int j = 0; j < w; j++) for (int k = 0; k < h; k++)
		{
			if (mat[j][k] == 'x') continue;
			if (j+1 < w)
			{
				if (mat[j+1][k] != 'x') g.AddEdge(w*h + j*h + k, (j+1)*h + k, 1);
				
			}
			if (k+1 < h && mat[j][k+1] != 'x') g.AddEdge(w*h + j*h + k, (j)*h + k+1, 1);
			if (k >0 && mat[j][k-1] != 'x') g.AddEdge(w*h+ j*h + k, (j)*h + k-1, 1);
			if (j >0 && mat[j-1][k] != 'x') g.AddEdge(w*h + j*h + k, (j-1)*h + k, 1);
		}
		for (int j = 0; j < w; j++)
			g.AddEdge(2*w*h,j*h,1);
		for (int j = 0; j < w; j++)
			g.AddEdge(w*h + j*h+h-1, 2*w*h+1,1);
		long long res = g.GetMaxFlow(2*w*h, 2*w*h+1);
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
}