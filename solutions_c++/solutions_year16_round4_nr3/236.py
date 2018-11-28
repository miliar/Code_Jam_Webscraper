#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              101
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int, int> pii;
int n, m, arr[MAXN], mr[] = {-1, 0, 1, 0}, mc[] = {0, 1 , 0, -1}, cnst;
string st[MAXN];
vector<int> adj[MAXN];
void build()
{
	Rep(i, MAXN) adj[i].clear();
	Rep(i, n) Rep(j, m) Rep(z, 4)
	{
		int nr = i + mr[z], nc = j + mc[z];
		if(nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
		if(st[i][j] == '/')
		{
			if(z == 0)
			{
				int ind1 = i * m + j;
				int ind2 = (n*m) + (nr * m + nc);
				adj[ind1].push_back(ind2);
			}
			else if(z == 1)
			{
				if(st[nr][nc] == '/')
				{
					int ind1 = (n*m) + (i * m + j);
					int ind2 = (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
				else
				{
					int ind1 = (n*m) + (i * m + j);
					int ind2 = (n*m) + (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
			}
			else if(z == 2)
			{
				int ind1 = (n*m) + (i * m + j);
				int ind2 = (nr * m + nc);
				adj[ind1].push_back(ind2);
			}
			else
			{
				if(st[nr][nc] == '*')
				{
					int ind1 = i * m + j;
					int ind2 = (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
				else
				{
					int ind1 = i * m + j;
					int ind2 = (n*m) + (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
			}
		}
		else
		{
			if(z == 0)
			{
				int ind1 = i * m + j;
				int ind2 = (n*m) + (nr * m + nc);
				adj[ind1].push_back(ind2);
			}
			else if(z == 1)
			{
				if(st[nr][nc] == '/')
				{
					int ind1 = (i * m + j);
					int ind2 = (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
				else
				{
					int ind1 = (i * m + j);
					int ind2 = (n*m) + (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
			}
			else if(z == 2)
			{
				int ind1 = (n*m) + (i * m + j);
				int ind2 = (nr * m + nc);
				adj[ind1].push_back(ind2);
			}
			else
			{
				if(st[nr][nc] == '*')
				{
					int ind1 = (n*m) + (i * m + j);
					int ind2 = (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
				else
				{
					int ind1 = (n*m) + (i * m + j);
					int ind2 = (n*m) + (nr * m + nc);
					adj[ind1].push_back(ind2);
				}
			}
		}
	}
	cnst = n*m * 2 + 1;
	int ind = cnst;
	Rep(i, m)
	{
		adj[ind].push_back(i);
		adj[i].push_back(ind);
		ind ++;
	}
	Rep(i, n)
	{
		if(st[i][m-1] == '/')
		{
			int ind2 = (n*m) + (i * m + m - 1);
			adj[ind].push_back(ind2);
			adj[ind2].push_back(ind);
		}
		else
		{
			int ind2 = (i * m + m - 1);
			adj[ind].push_back(ind2);
			adj[ind2].push_back(ind);
		}
		ind++;
	}
	for(int i = m - 1; i>=0; i--)
	{
		int ind2 = (n*m) + ((n-1) * m + i);
		adj[ind].push_back(ind2);
		adj[ind2].push_back(ind);
		ind++;
	}
	for(int i = n-1; i>=0; i--)
	{
		if(st[i][0] == '*')
		{
			int ind2 = (n*m) + (i * m);
			adj[ind].push_back(ind2);
			adj[ind2].push_back(ind);
		}
		else
		{
			int ind2 = (i * m);
			adj[ind].push_back(ind2);
			adj[ind2].push_back(ind);
		}
		ind++;
	}
}
int col[MAXN];
bool DFS(int p, int c)
{
	if(col[p] == c) return 1;
	if(col[p] != 0) return 0;
	col[p] = c;
	Rep(i, adj[p].size())
	{
		int nx = adj[p][i];
		bool ret = DFS(nx, c);
		if(!ret) return 0;
	}
	return 1;
}
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas = 1;
	cin>>tc;
	while (tc--)
	{
		PF("Case #%d:\n", cas++);
		bool pr = 0;
		cin>>n>>m;
		Rep(i, 2*(n+m)) 
		{
			cin>>arr[i];
			arr[i]--;
		}
		Rep(msk, 1<<(n*m))
		{
			Rep(i, n) 
			{
				st[i].clear();
				Rep(j, m)
				{
					if(msk&(1<<((i*m) + j))) st[i] += "/";
					else st[i]+="*";
				}
			}
			build();
			Set(col, 0);
			bool ok = 1;
			for(int i = 0; i<2*(n+m); i+=2)
			{
				ok = DFS(cnst + arr[i], arr[i]+cnst);
				if(!ok) break;
				if(col[cnst + arr[i+1]] != arr[i]+cnst)
				{
					ok = 0;
					break;
				}
			}
			if(ok)
			{
				pr = 1;
				Rep(i, n) 
				{
					Rep(j, m) if(st[i][j] == '/') cout<<st[i][j];
					else cout<<"\\";
					cout<<endl;
				}
				break;
			}
		}
		if(pr == 0)
		{
			PF("IMPOSSIBLE\n");
		}
	}
	return 0;
}