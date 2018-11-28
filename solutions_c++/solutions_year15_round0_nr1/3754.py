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
	int t, u;
    si(t);
    u = t;
    while(t--) {
        int n, cnt = 0, ans = 0;
        string s;
        si(n);
        cin>>s;
        fr(i, n + 1) {
            if(s[i] - '0' > 0) {
                if(cnt < i) {
                    ans += i - cnt;
                    cnt = i;
                }
                cnt += s[i] - '0';
            }
        }
        cout<<"Case #"<<u - t<<": "<<ans<<endl;
    }
	return 0;
}
