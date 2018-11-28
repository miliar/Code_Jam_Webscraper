#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define DEB(x) cout<<#x<<" : "<<x<<endl;
const ll mod = 1000000007LL;
const int lmt = 100005;

string s, ans;

int main(){
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    S(t);
    for(int tst = 1; tst <= t; tst++){
        ans = "";
        cin>>s;
        ans = ans + s[0];
        for(int i = 1; i < s.size(); i++){
            if(s[i] >= ans[0]){
                ans = s[i] + ans;
            }
            else{
                ans = ans + s[i];
            }
        }
        printf("Case #%d: ",tst);
        cout<<ans;
        nl;
    }
    return 0;
}