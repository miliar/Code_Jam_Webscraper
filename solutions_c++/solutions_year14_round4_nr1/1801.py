#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1001],c[1001],cnt[1001];
int cmp(int x,int y){
    if (x>y) return 1;
    return 0;
}
void clear();

int main(){
     FILE *fp;
     int t,ri,i,j,n,cap,top,f,ii;
     fp=fopen("A.out","w");
     scanf("%d",&t);
     for (ri=1;ri<=t;ri++){
         clear();
         scanf("%d %d",&n,&cap);
         for (i=1;i<=n;i++)
             scanf("%d",&a[i]);
         sort(a+1,a+n+1,cmp);
         for (ii=1;ii<=n;ii++) printf("%d ",a[ii]);
                 printf("\n");
         top=0;
         for (i=1;i<=n;i++){
             f=1;
             for (j=1;j<=top;j++)
                 if ((cnt[j]<2)&&(c[j]+a[i]<=cap)&&f){
                    c[j]+=a[i];
                    cnt[j]++;
                    f=0;
                 }
             if (f==1){
                       top++;
                       c[top]=a[i];
                       cnt[top]=1;
                       }
             for (ii=1;ii<=n;ii++) printf("%d ",c[ii]);
                 printf("\n");
         }
         fprintf(fp,"Case #%d: %d\n",ri,top);
     }
     return 0;
}

void clear(){
     int i;
     for (i=1;i<=1000;i++){
         a[i]=0;
         c[i]=0;
         cnt[i]=0;
     }
}
                 
