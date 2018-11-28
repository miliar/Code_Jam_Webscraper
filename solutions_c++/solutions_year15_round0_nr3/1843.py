#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int multable[][5] = {{0,0,0,0,0},
                           {0,1,2,3,4},
                           {0,2,-1,4,-3},
                           {0,3,-4,-1,2},
                           {0,4,3,-2,-1}};
const int MAXN = 10005;
int l,x,s[MAXN],fac,pre[MAXN];
bool flag;
char buf[MAXN];

int mul(int a,int b){
    int sgn = a * b < 0 ? -1 : 1;
    a = a < 0 ? -a : a; b = b < 0 ? -b : b;
    return sgn * multable[a][b];
}

int main(){
    freopen("input","r",stdin);
    freopen("out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1;cas <= T;++ cas){
        printf("Case #%d: ",cas);
        scanf("%d%d",&l,&x);
        scanf("%s",buf);
        for(int i = 0;i < l;++ i)
            s[i] = buf[i] == 'i' ? 2 : buf[i] == 'j' ? 3 : 4;
        fac = 1;
        for(int i = 0,lim = x * l,now;i < lim;++ i){
            now = i % l;
            fac = mul(fac,s[now]);
            pre[i] = fac;
            /*
            printf("pre%d : %d\n",i,fac);
            */
        }
        fac = 1;
        flag = false;
        for(int i = x * l - 1,now;i >= 0;-- i){
            now = i % l;
            fac = mul(s[now],fac);
            /*
            printf("suf%d : %d\n",i,fac);
            */
            if(fac == 4){
                int tot = 1;
                for(int j = i - 1;j > 0;-- j){
                    tot = mul(s[j % l],tot);
                    if(tot == 3 && pre[j - 1] == 2){
                        flag = true; break;
                    }
                }
                if(flag) break;
            }
        }
        printf("%s\n",flag ? "YES" : "NO");
    }
    return 0;
}
