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
int sum,r,n,t,txt,N;
#define S 1005
char ch[S];
int main() {
	int i,j,k;
    freopen("a_large.in", "r", stdin);
    freopen("a_large.out", "w", stdout);
    scanf("%d",&t);
    while(t--){
        printf("Case #%d: ", ++txt);
        int len;
        scanf("%d %s",&len, ch);
        int ans = 0;
        int cur = 0;
        for(int i = 0; i <= len; ++i)if(ch[i] != '0'){
            if(cur < i){
                int diff = i - cur;
                ans += diff;
                cur += diff;
            }
            cur += (ch[i] - '0');
        }
        printf("%d\n",ans);
    }
	return 0;
}








