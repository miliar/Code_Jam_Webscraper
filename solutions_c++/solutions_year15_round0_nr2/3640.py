/*
	Aditya Sharma
	IIIT Allahabad
*/
#include <bits/stdc++.h>
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ss(n) scanf("%s",n)
#define fr(i, n) for(int i = 0; i < n; i++)
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define REN(i, a, b) for (int i = int(a); i >= int(b); i--)
#define ms(i, n) memset(i, n, sizeof(i))
#define INF 1002000000
#define MOD 1000000007
typedef long long LL;
using namespace std;
int main ()
{
	//freopen ("input2.in","r",stdin);
	//freopen ("output2.out","w",stdout);
	int t, d, u, mini, maxi, ans,p[1004];
    si(t);u = t;
    while(t--) {
        si(d);
        maxi = 0;
        fr(i, d) {
            si(p[i]);
            maxi = max(maxi, p[i]);
        }
        mini = INF;
        REP(j, 1, maxi) {
            ans = 0;
            fr(i, d) {
                ans += (p[i] / j) - ((p[i] % j == 0) ? 1:0);
            }
            //cout<<ans<<endl;
            mini = min(ans + j, mini);
        }
        cout<<"Case #"<<u - t<<": "<<mini<<endl;
    }
	return 0;
}
