#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
double naomi[1001],ken[1001],c[1001];
bool cmp(const double &x,const double &y);
int judge(double a[],double b[],int n);

int main(){
    FILE *fp;
    int t,n,ri,i,ans1,ans2;
    scanf("%d",&t);
    fp=fopen("4.out","w");
    for (ri=1;ri<=t;ri++){
        scanf("%d",&n);
        for (i=1;i<=n;i++)
            scanf("%lf",&naomi[i]);
        for (i=1;i<=n;i++)
            scanf("%lf",&ken[i]);
        sort(naomi+1,naomi+n+1,cmp);
        sort(ken+1,ken+n+1,cmp);
        for (i=1;i<=n;i++)
            printf("%.2lf ",naomi[i]);
        printf("\n");
        for (i=1;i<=n;i++)
            printf("%.2lf ",ken[i]);
        printf("\n");
        
        ans1=judge(naomi,ken,n);
        ans2=judge(ken,naomi,n);
        fprintf(fp,"Case #%d: %d %d\n",ri,ans1,n-ans2);
    }
    return 0;
}

bool cmp(const double &x,const double &y){
     if (x>y) return true;
     return false;
}

int judge(double a[],double b[],int n){
    int i,j,rs=0;
    for (i=1;i<=n;i++)
        c[i]=a[i];
    for (i=1;i<=n;i++){
        j=1;
        while ((c[j+1]>b[i])&&(j<n-i+1)) j++;
        if (c[j]>b[i]){
           rs++;
           while (j<n-i+1){
                 c[j]=c[j+1];
                 j++;
           }
        }
    }
    return rs;
}
        
