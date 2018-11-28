#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

#define MAXN 110
using namespace std;

typedef long long LL;

char s[MAXN];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,k,t,n;
    scanf("%d%d%d",&t,&n,&j); printf("Case #1:\n");
    s[0]=s[n-1]='1'; s[n]='\0';
    for(i=1;i<=j;++i){
        for(k=0;k*2<n-2;++k)
            s[k+1]=s[n-k-2]=(i&(1<<k))?'1':'0';
        printf("%s",s);
        for(k=2;k<=10;++k) printf(" %d",(k&1)?2:(k+1));
        printf("\n");
    }
    return 0;
}
