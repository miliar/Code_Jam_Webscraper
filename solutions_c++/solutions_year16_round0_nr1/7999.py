#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;


#define LL long long
#define N 200020
#define M 3000011
#define MP make_pair
#define Pi acos(-1.0)
#pragma comment(linker,"/STACK:1024000000,1024000000")
#define ls (rt << 1)
#define rs (ls | 1)
#define md ((ll+rr)/2)
#define lson ll, md, ls
#define rson md+1, rr, rs
#define mod 1000000007
#define inf 0x3f3f3f3f
#define sqr(x) ((x)*(x))
#define eps 1e-6
#define MP make_pair
#define uLL unsigned long long
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
#define F(x) ((x)/3+((x)%3 == 1 ? 0 : tb))
#define G(x) ((x)<tb ? (x)*3+1 : ((x) - tb)*3+2)
#define lowbit(x) ((x)&(-x))

string s;
int dp[105][2];


int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T,casi = 0;
    cin>>T;
    while(T--){
        printf("Case #%d: ",++casi);
        int n,now = 0,ans = 0;
        cin>>n;
        if(n == 0){
            puts("INSOMNIA");
            continue;
        }
        for(int i=n;;i+=n){
            int tmp = i;
            while(tmp){
                now |= (1<<(tmp%10));
                tmp /= 10;
            }
            ans = i;
            if(now == (1<<10)-1) break;
        }
        printf("%d\n",ans);
    }
    return 0;
}