
#include<cstdio>
#include<cstring>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<bitset>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<cstdlib>
#include<cmath>
#define PI 2*asin(1.0)
#define LL __int64
#define pb push_back
#define clr(a,b) memset(a,b,sizeof(a))
#define lson lr<<1,l,mid
#define rson lr<<1|1,mid+1,r
const int  MOD = 1e9 + 7;
const int N = 5e4 + 15;
const int INF = (1 << 31) - 10;
const int letter = 130;
using namespace std;
char str[15];
int n;
int main() {
    freopen("AC.in","r",stdin);
    freopen("GOOGLE.txt","w",stdout);
    int tc;
    int cas = 0;
    scanf("%d", &tc);
    while(tc--) {
        scanf("%d%s", &n, str);
        int len = strlen(str);
        for(int i = 0; i < len; i++) str[i] = str[i] - '0';
        int sum = 0;
        int pt = str[0];
        int tc;
        for(int i = 1; i < len; i++) {
            tc = 0;
            if(i > pt) {
                sum += (i - pt);
                tc = i-pt;
            }
            pt += str[i];
            pt += tc;
        }
        printf("Case #%d: %d\n", ++cas, sum);

    }
    return 0;
}
