#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;
typedef long long LL;

LL k,c,s;

int main(){
    int i,j,cas;
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&cas);
    for(int T=1;T<=cas;T++){
        scanf("%I64d%I64d%I64d",&k,&c,&s);
        LL tmp = 1;
        for(i = 1;i < c;i++) tmp *= k;
        printf("Case #%d:",T);
        for(i = 0;i < k;i++) printf(" %I64d",tmp*i+1);
        putchar('\n');
    }


    return 0;
}
