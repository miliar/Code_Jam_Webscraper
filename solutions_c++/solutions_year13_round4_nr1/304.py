#include<cstdio>
#include<cstdlib>
#include<algorithm>

const int MAXN = 1000+2;
const long long mask = 1000002013;
int oo[MAXN];
int oe[MAXN];
int o[MAXN];
int e[MAXN];
int p[MAXN];
int sk[MAXN];
int left[MAXN];
int top;
long long res;
int n,m,noc;

inline long long pp(int n,int i){
    long long res = n;
    res += n+1-i;
    res *= i;
    return (res/2)%mask;
}

bool cmp1(const int& lhs,const int& rhs){
    return o[lhs]<o[rhs];
}
bool cmp2(const int& lhs,const int& rhs){
    return e[lhs]<e[rhs];
}

void pushp(int x){
    sk[top] = x;
    left[top] = p[x];
    ++top;
}
void popp(int x){
    int count = p[x];
    while (count>0){
        int tmp = (count>left[top-1])?left[top-1]:count;
        long long r = pp(n,e[x]-o[sk[top-1]])*tmp;
        r %= mask;
        res -= r;
        if (res<0){
            res += mask;
        }
        count -= tmp;
        left[top-1] -= tmp;
        if (left[top-1]==0){
            --top;
        }
    }
}

int main(int argc,char* argv[]){
    //freopen("ain.txt","r",stdin);
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        printf("Case #%d: ",tnoc);
        scanf("%d%d",&n,&m);
        res = 0;
        for (int i=0;i<m;++i){
            scanf("%d%d%d",&o[i],&e[i],&p[i]);
            oo[i] = i;
            oe[i] = i;
            res += (pp(n,e[i]-o[i])*p[i])%mask;
        }
        res %= mask;
        std::sort(oo,oo+m,cmp1);
        std::sort(oe,oe+m,cmp2);
        int ino = 0;
        int ine = 0;
        while (ino!=m || ine!=m){
            if (ino==m){
                while (ine!=m){
                    popp(oe[ine]);
                    ++ine;
                }
            } else if (o[oo[ino]]<=e[oe[ine]]){
                pushp(oo[ino]);
                ++ino;
            } else {
                popp(oe[ine]);
                ++ine;
            }
        }
        printf("%d\n",res);
    }
    return 0;
}
