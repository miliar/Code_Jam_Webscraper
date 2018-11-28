#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Edge
{
public:
	int st, dest;
	Edge(int a,int b)
	{
		st = a;
		dest = b;
	}
};
vector<Edge> edges[100];
bool graph[100][100];

class City
{
public:
	string zip;
	int num;
};
City cities[100];

int Tn;
int n,m;
//string zips[100];
int num[100];

string ans;
bool used[100];
int nodemap[100];

int chain[100];

void selectsort()
{
	for (int i=1;i<n;i++)
		for (int j=i+1;j<=n;j++)
			if (cities[i].zip > cities[j].zip)
			{
				City tmp = cities[i];
				cities[i] = cities[j];
				cities[j] = tmp;
			}
}

void dfs(int x, int num, string cur,int ret)
{
	used[x] = true;
	num++;
	cur += cities[x].zip;
	if (num==n)
	{
		if (ans=="" || ans > cur)
			ans = cur;
		return;
	}
	for (int i=1;i<=n;i++)
		if (!used[i])
			for (int j=ret;j>=0;j--)
			{
				int node = cities[chain[j]].num;
				if (graph[node][cities[i].num])
				{
					int newchain[100];
					memcpy(newchain, chain, sizeof chain);
					chain[j+1] = i;
					dfs(i, num, cur, j+1);
					memcpy(chain, newchain, sizeof chain);
				}
			}
	
	used[x] = false;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		cin >> n >> m;
		cin.ignore();
		for (i=1;i<=n;i++)
		{
			getline(cin, cities[i].zip);
			cities[i].num = i;
			edges[i].clear();
		}
		memset(graph,0, sizeof graph);
		for (i=0;i<m;i++)
		{
			int a,b;
			cin >> a >> b;
			graph[a][b] = graph[b][a] = true;
			edges[a].push_back(Edge(a,b));
			edges[b].push_back(Edge(b,a));
		}
		selectsort();
		for (i=1;i<=n;i++)
			nodemap[cities[i].num] = i;

		ans = "";
		memset(used, 0, sizeof used);
		chain[0] = 1;
		dfs(1,0,"",0);


		cout << "Case #" << T << ": " << ans << endl;

	}
}