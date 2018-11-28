#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


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
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n, m, cc, one[1<<26], mr[]={-1, -1, -1, 0, 1, 1, 1, 0}, mc[]={-1, 0, 1, 1, 1, 0, -1, -1}, bmb[5][5], tot;
char st[60][60];
int cnt(int x)
{
	if(x==0) return 0;
	if(~one[x]) return one[x];
	return one[x]=cnt(x/2) + (x&1);
}
bool vis[5][5];
void DFS(int r, int c)
{
	tot++;
	vis[r][c]=1;
	if(bmb[r][c]) return;
	Rep(j, 8)
	{
		int nr=r+mr[j], nc=c+mc[j];
		if(nr>=n || nr<0 || nc<0 || nc>=m || vis[nr][nc]) continue;
		DFS(nr, nc);
	}
}
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t=1, tc;
	cin>>tc;
	Set(one, -1);
	Rep(i, 1<<26) cnt(i);
	while (tc--)
	{
		bool imp=1;
		PF("Case #%d:\n", t++);
		cin>>n>>m>>cc;
		if(n*m-cc==1) 
		{
			imp=0;
			Rep(i, n) Rep(j, m) st[i][j]='*';
			st[0][0]='c';
		}
		else if(cc==0)
		{
			imp=0;
			Rep(i, n) Rep(j, m) st[i][j]='.';
			st[0][0]='c';
		}
		else Rep(i, 1<<((m*n)+1)) if(one[i]==cc)
		{
			Set(vis, 0);
			Set(bmb, 0);
			int x=i;
			for(int r=n-1; r>=0; r--) for(int c=m-1; c>=0; c--) 
			{
				if(x&1)
				{
					st[r][c]='*';
					bmb[r][c]++;
					Rep(j, 8) 
					{
						int nr=r+mr[j], nc=c+mc[j];
						if(nr>=n || nr<0 || nc<0 || nc>=m) continue;
						bmb[nr][nc]++;
					}
				}
				else st[r][c]='.';
				x/=2;
			}
			for(int r=n-1; r>=0; r--) for(int c=m-1; c>=0; c--)  if(bmb[r][c]==0 && st[r][c]!='*')
			{
				tot=0;
				DFS(r, c);
				if(tot==(n*m)-cc)
				{
					st[r][c]='c';
					imp=0;
				}
				r=-1;
				break;
			}
			if(imp==0) break;
		}
		if(imp) PF("Impossible\n");
		else Rep(i, n)
		{
			Rep(j, m) cout<<st[i][j];
			cout<<endl;
		}
	}
	return 0;
}