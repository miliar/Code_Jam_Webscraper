/*#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <tuple>
#include <fstream>*/
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define INF 1001001001
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define VI vector<int>
#define VII vector<pair<int,int> > 
#define VS vector<string>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
//template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);
//#define LOCAL_TEST

vector<string> grid;

int solve()
{
	grid.clear();
	int r,c;
	cin>>r>>c;
	//cout<<" r c "<<r<<" "<<c<<endl;
	REP(i,r)
	{
		string s;
		cin>>s;
		//cout<<s<<endl;
		grid.pb(s);
	}
	int res=0;
	/*REP(i,r)
	{
		REP(j,c)cout<<grid[i][j];
		cout<<endl;
	}*/
	REP(i,r)
	{
		REP(j,c)
		{
			if(grid[i][j] == '<')
			{
				//cout<<"lewo "<<i<<" "<<j<<endl;
				bool ok=0;
				for(int k=j-1; k>=0; k--)
				{
					if(grid[i][k] != '.')ok = 1;
				}
				if(ok)continue;
				bool found = 0;
				REP(k,r)
				{
					if(k==i)continue;
					if(grid[k][j] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				REP(k,c)
				{
					if(k==j)continue;
					if(grid[i][k] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				cout<<"IMPOSSIBLE\n";
				return 0;
			}
			else if(grid[i][j] == '^')
			{
				//cout<<"gora "<<i<<" "<<j<<endl;
				bool ok=0;
				for(int k=i-1; k>=0; k--)
				{
					if(grid[k][j] != '.')ok = 1;
				}
				if(ok)continue;
				bool found = 0;
				REP(k,r)
				{
					if(k==i)continue;
					if(grid[k][j] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				REP(k,c)
				{
					if(k==j)continue;
					if(grid[i][k] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				cout<<"IMPOSSIBLE\n";
				return 0;
			}
			else if(grid[i][j] == '>')
			{
				bool ok=0;
				//cout<<"prawo "<<i<<" "<<j<<endl;
				for(int k=j+1; k<c; k++)
				{
					//cout<<"checking "<<i<<" "<<k<<endl;
					if(grid[i][k] != '.')ok = 1;
				}
				if(ok)continue;
				bool found = 0;
				REP(k,r)
				{
					if(k==i)continue;
					if(grid[k][j] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				REP(k,c)
				{
					if(k==j)continue;
					if(grid[i][k] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				cout<<"IMPOSSIBLE\n";
				return 0;
			}
			else if(grid[i][j] == 'v')
			{
				//cout<<"dol "<<i<<" "<<j<<endl;
				bool ok=0;
				for(int k=i+1; k<r; k++)
				{
					if(grid[k][j] != '.')ok = 1;
				}
				if(ok)continue;
				bool found = 0;
				REP(k,r)
				{
					if(k==i)continue;
					if(grid[k][j] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				REP(k,c)
				{
					if(k==j)continue;
					if(grid[i][k] != '.')
					{
						res++;
						//cout<<"adding for "<<i<<" "<<j<<endl;
						found = 1;
						break;
					}
				}
				if(found)continue;
				cout<<"IMPOSSIBLE\n";
				return 0;
			}
		}
	}
	cout<<res<<"\n";
	return 0;
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	IOS
	cout << fixed << setprecision(16);
	int ret = MAIN();
	#ifdef LOCAL_TEST
		cout << "[Finished in " << clock() - start << " ms]" << endl;
	#endif
	return ret;
}