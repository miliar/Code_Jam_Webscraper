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

bool check(int x){
    if(x == ((1<<10) - 1))
        return true;
    return false;
}

int main(){
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    S(t);
    for(int tst = 1; tst <= t; tst++){
        int n;
        S(n);
        if(n == 0){
            printf("Case #%d: INSOMNIA\n", tst);
            continue;
        }
        ll x, ans;
        int mask = 0;
        for(int i = 1; !check(mask); i++){
            x = n;
            x *= i;
            ans = x;
            while(x > 0){
                int d = x%10;
                mask |= (1<<d);
                x /= 10;
            }
        }
        printf("Case #%d: %lld\n",tst,ans);
    }
    return 0;
}