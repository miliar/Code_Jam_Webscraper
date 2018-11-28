#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<time.h>
#include<queue>
#include<stack>
#include<iterator>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<set>
#include<map>
//#define ONLINE_JUDGE
#define eps 1e-5
#define INF 0x7fffffff
#define FOR(i,a) for((i)=0;i<(a);(i)++)
#define MEM(a) (memset((a),0,sizeof(a)))
#define sfs(a) scanf("%s",a)
#define sf(a) scanf("%d",&a)
#define sfI(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfI(a) printf("%I64d\n",a)
#define pfs(a) printf("%s\n",a)
#define sfd(a,b) scanf("%d%d",&a,&b)
#define sft(a,b,c)scanf("%d%d%d",&a,&b,&c)
#define for1(i,a,b) for(int i=(a);i<b;i++)
#define for2(i,a,b) for(int i=(a);i<=b;i++)
#define for3(i,a,b)for(int i=(b);i>=a;i--)
#define MEM1(a) memset(a,0,sizeof(a))
#define MEM2(a) memset(a,-1,sizeof(a))
const double PI=acos(-1.0);
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}
template<class T> T lcm(T a,T b){return a/gcd(a,b)*b;}
template<class T> inline T Min(T a,T b){return a<b?a:b;}
template<class T> inline T Max(T a,T b){return a>b?a:b;}
using namespace std;
//#define ll __int64
#define pi acos(-1.0);
int n,m;
#define Mod 1000000007
#define N 510
#define M 1000100
const int size = 10010;
const int mod = 9901;
int a[M];
int mmax;
int main(){
//#ifndef ONLINE_JUDGE
//    freopen("in.txt","r",stdin);
//  freopen("out.txt","w",stdout);
//#endif
    int t;
    int kas = 1;
    sf(t);
    int s;
    char ch[1010];
    while(t--){
    	sf(s);
    	sfs(ch);
    	int len = strlen(ch);
    	int peo = 0;
    	int ans = 0;
    	for(int i=0;i<len;i++){
    		if(peo<i){
    			ans += (i-peo);
    			peo = i+(ch[i]-'0');
    		}else{
    			peo += (ch[i]-'0');
    		}
    	}
    	printf("Case #%d: %d\n",kas++,ans);
    }
return 0;
}
