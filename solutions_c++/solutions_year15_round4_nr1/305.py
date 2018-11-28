//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)


map<pll,bool> safe;
string graph[111];
char dir[] = {'^','>','v', '<'};
map<char,ll> mydir;

ll dc[] = {0,1,0,-1};
ll dr[] = {-1,0,1,0};
int main()
{
	mydir['^'] = 0;
	mydir['>'] = 1;
	mydir['v'] = 2;
	mydir['<'] = 3;
	ll test;
	sl(test);
	repii(tt,1,test)
	{
		printf("Case #%lld: ", tt);
		ll r,c;
		cin>>r>>c;
		safe.clear();
		repi(i,0,r)
			cin>>graph[i];
		ll ans = 0;
		bool impossible = false;
		repi(i,0,r)
			repi(j,0,c)
			{
				bool ok[4];
				repi(d,0,4)
				{
					ok[d] = false;
					ll ii = i;
					ll jj = j;
					ii += dr[d];
					jj += dc[d];
					while(ii<r &&ii>=0 && jj<c && jj>=0)
					{
						if(graph[ii][jj] != '.')
							ok[d] = true;
						ii += dr[d];
						jj += dc[d];
					}
				}
				if(graph[i][j] == '.' || ok[mydir[graph[i][j]]]);
					
				else if(ok[0] or ok[1] or ok[2] or ok[3])
				{
					ans++;
				}
				else
					impossible = true;
			}
		if(impossible)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;

	}
	return 0;
}