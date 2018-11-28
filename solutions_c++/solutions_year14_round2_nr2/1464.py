#include <stdio.h>
FILE *fp;
int main(){
    int a,b,k,t,ri,i,j,ans;
    scanf("%d",&t);
    fp=fopen("b.txt","w");
    for (ri=1;ri<=t;ri++){
        ans=0;
        scanf("%d%d%d",&a,&b,&k);
        for (i=0;i<a;i++)
        for (j=0;j<b;j++)
            if ((i&j)<k) {
                       //printf("%d\n",i&j);
                       ans++;
                       }
            //printf("%d\n",i&j);
        fprintf(fp,"Case #%d: %d\n",ri,ans);
    }
    return 0;
}
