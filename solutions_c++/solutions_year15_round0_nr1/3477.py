/*pranjuldb*/
#include <bits/stdc++.h>
#define pri(a) printf("%d",a)
#define prl(a) printf("%lld",a)
#define prd(a) printf("%lf",a)
#define nl printf("\n")
#define sp printf(" ")
#define prs(str) printf("%s", str)
#define pb push_back
#define mem(a,b) memset(a, b, sizeof(a))
#define vi vector < int >
#define vl vector < long long int >
#define pll pair<long long, long long>
#define pii pair < int , int >
#define ll long long
#define rep(i,j,k) for(i = j; i < k; i++)
#define nrep(i,j,k) for(i = j; i >= k; i--)
#define scs(str) scanf("%s", str)
#define sci(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define scd(a) scanf("%lf", &a)
#define fr first
#define se second
#define mp make_pair

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, i, j;
    sci(t);
    int n;
    string s;
    rep(j, 1, t + 1){
        cin >> n;
        cin >> s;
        int sum = 0;
        int ans = 0;
        rep(i, 0, n + 1) {
            if(s[i] - 48 >= 0) {
                if(sum < i) {
                    ans += (i - sum);
                    sum += (i - sum);
                }
            }
            sum += s[i] - 48;
        }
        cout << "Case #" << j << ": " << ans << endl;
    }
}

