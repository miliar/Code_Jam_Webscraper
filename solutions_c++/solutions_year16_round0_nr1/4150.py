#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
#define INF 1e8
#define maxn 2005+10
#define maxm 100086+10
#define mod 7
#define eps 1e-7
#define PI acos(-1.0)
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%I64d",&n)
#define scan2(n,m) scanf("%d%d",&n,&m)
#define scans(s) scanf("%s",s);
#define ini(a) memset(a,0,sizeof(a))
#define out(n) printf("%d\n",n)
using namespace std;
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
bool vis[10] = {0};
bool check()
{
	for(int i = 0;i < 10; i++)
	{
		if(!vis[i]) return false;
	}
	return true;
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif  
	int T;
	cin>>T;
	int cas = 1;
	while(T--)
	{
		printf("Case #%d: ",cas++);
		ll n;
		cin>>n;
		ini(vis);
		bool ok = 0;
		for(ll i = 1;i <= 100000; i++)
		{
			ll x = i * n;
			while(x)
			{
				vis[x % 10] = 1;
				x /= 10;
			}
			if(check())
			{
				cout<<i*n<<endl;
				ok = 1;
				break;
			}
		}
		if(!ok) cout<<"INSOMNIA\n";
	}
    return 0;
}