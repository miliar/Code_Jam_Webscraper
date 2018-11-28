#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1001],b[1001];
int cmp(int x,int y){
    if (x>y) return 1;
    return 0;
}
int findmin(int n);

int main(){
    FILE *fp;
    int t,ri,i,j,n,nl,min,ans;
    scanf("%d",&t);
    fp=fopen("B.txt","w");
    for (ri=1;ri<=t;ri++){
        scanf("%d",&n);
        ans=0;
        nl=n;
        for (i=1;i<=n;i++)
            scanf("%d",&a[i]);
        for (i=1;i<=n;i++){
            min=findmin(nl);
            if (min-1<nl-min) ans+=min-1;
            else ans+=nl-min;
            for (j=min;j<nl;j++)
                a[j]=a[j+1];
            /*for (j=1;j<nl;j++)
                printf("%d ",a[j]);*/
            nl--;
            printf("\n");
        }
        fprintf(fp,"Case #%d: %d\n",ri,ans);
    }
    return 0;
}

int findmin(int n){
    int i,min=1000000001,ind;
    for (i=1;i<=n;i++)
        if (a[i]<min){
           ind=i;
           min=a[i];
        }
    return ind;
}
