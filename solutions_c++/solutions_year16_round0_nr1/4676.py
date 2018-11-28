#include<iostream> 
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<set>
#include<sstream>
#include<cstring>
#include<string>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;
#define eps 1e-8
#define inf (1<<30)
#define pi (2*acos(0.0))
#define all(a) a.begin(),a.end()
#define mem(a,v) memset(a,v,sizeof(a))
#define rep(i,b,e) for((i)=b;(i)<(e);(i)++)
#define rev(i,b,e) for((i)=e-1;(i)>=(b);(i)--)
#define fi(b,e) for((i)=b;(i)<(e);(i)++)
#define fj(b,e) for((j)=b;(j)<(e);(j)++)
typedef long long LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
int sum,r,t,txt,N;
int d[12], cases;
#define S 1000005
char ch[22];
LL n;
int markDigits(LL v){
    sprintf(ch, "%lld", v);
    for(int i = 0; ch[i]; ++i){
        d[ ch[i] - '0' ] = 1;
    }
    for(int i = 0; i <= 9; ++i)if(!d[i])return false;
    return true;
}
int main() {
    int i,j,k;
    freopen("a_large.in", "r", stdin);
    freopen("a_large.out", "w", stdout);
    scanf("%d", &t);
    while(t--){
        scanf("%lld",&n);
        memset(d, 0, sizeof d);
        int found = 0;
        int ok = markDigits(n);
        LL nn = n;
        for(int i = 1; i < S; ++i){
            n += nn; 
            ok = markDigits(n);
            if(ok){
                printf("Case #%d: %lld\n", ++cases, n);
                found = 1;
                break;
            }
        }
        if(!found)printf("Case #%d: INSOMNIA\n", ++cases);
    }

    return 0;
}








