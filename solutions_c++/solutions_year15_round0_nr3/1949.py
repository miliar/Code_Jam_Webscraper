#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<vector>
#include<bitset>
#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define eps 1e-6
#define pi acos(-1.0)
using namespace std;
typedef long long ll;
const int maxn = 1000000 + 10;
int table[4][4] = {
{0,1,2,3},
{1,4,3,6},
{2,7,4,1},
{3,2,5,4},
};
inline int cal (int x,int y) {
    int sign = 0;
    if(x > 3) {
        x -= 4;
        sign ^= 1;
    }
    if(y > 3) {
        y -= 4;
        sign ^= 1;
    }
    int res = table[x][y];
    if(res > 3) {
        res -= 4;
        sign ^= 1;
    }
    if(sign) res += 4;
    return res;
}
char str[maxn],S[10010];
int copystr(int n,int t) {
    int len = 0;
    for(int i = 0;i < t;++i) {
        for(int j = 0;j < n;++j)
            str[len++] = S[j];
    }
    return len;
}
int main()
{
   // freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    int t,tcase = 0;
    cin>>t;
    while(t--) {
        tcase++;
        ll X,n;
        cin>>n>>X;
        cin>>S;
        if(X*n > 1000000) {
            X = (X - 1000000/n)/4;
            if((X + 4)*n <= 1000000)
                X += 4;
            if(X*n > 1000000)
                X -= 4;
        }
        n = copystr(n,X);
        int step = 0,a = 0,b = 0;
        for(int i = 0;i < n;++i) {
            b = str[i] - 'i' + 1;
            a = cal(a,b);
            if(step == 0 && a == 1) {
                step++;
                a = 0;
            }
            else if (step == 1 && a == 2) {
                step++;
                a = 0;
            }
            else if (step == 2 && a == 3) {
                step++;
            }
        }
        printf("Case #%d: ",tcase);
        if(step == 3 && a == 3)
            printf("YES\n");
        else
            printf("NO\n");

    }
    return 0;
}
