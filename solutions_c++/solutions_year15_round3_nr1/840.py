/*

    Harsh Vardhan :)

*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<queue>
#include<stack>

using namespace std;

#define MAX 1111111
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define tr(v, it) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define mp make_pair
#define F first
#define S second
#define SET(p,v) memset(p, v, sizeof(p))
#define chkC(x,n) (x[n>>6]&(1<<((n>>1)&31)))
#define setC(x,n) (x[n>>6]|=(1<<((n>>1)&31)))
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;


int main()
{
    freopen("H:\\input.txt","r",stdin);
    freopen("H:\\output.txt","w",stdout);
	int t;
	gi(t);
	for(int i=1;i<=t;i++)
    {
        int ans = 0,r,c,w;
		cin >> r >> c >> w;
		ans = c / w *r;
		ans += w - 1;
		if (c%w != 0)
			ans++;
		cout << "Case #" << i << ": " << ans << endl;
    }

     return 0;
 }