#include <iostream>
#include <stdlib.h>
using namespace std;
const int maxn = 10005;
int a[maxn],n,m;
int cmp(const void *A,const void *B)
{
    return (*(int *)A)-(*(int *)B);
}
void init()
{
     scanf("%d%d",&n,&m);
     int i;
     for(i=1;i<=n;i++)scanf("%d",&a[i]);
     qsort(a+1,n,sizeof(a[1]),cmp);
}
void work()
{
     int i,p=n,s;
     s=n;
     for(i=1;i<=n;i++){
                       while(p>i&&a[p]+a[i]>m)--p;
                       if(p<=i)break;
                       --s;
                       --p;
                       }
     printf("%d\n",s);
}
int main(void)
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int tc,i=0;
    scanf("%d",&tc);
    while(tc--){
                printf("Case #%d: ",++i);
                init();
                work();
                }
    return 0;
}
