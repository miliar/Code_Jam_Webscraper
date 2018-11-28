#include <stdio.h>
int main(){
    FILE *fp;
    int a[4][4],b[4][4];
    int ans1,ans2,t,ri,i,j,c,rs;
    scanf("%d",&t);
    fp=fopen("1.txt","w");
    for (ri=1;ri<=t;ri++){
        scanf("%d",&ans1);
        for (i=0;i<4;i++)
        for (j=0;j<4;j++)
            scanf("%d",&a[i][j]); 
        scanf("%d",&ans2);
        for (i=0;i<4;i++)
        for (j=0;j<4;j++)
            scanf("%d",&b[i][j]);
        
        c=0;
        for (i=0;i<4;i++)
        for (j=0;j<4;j++)
            if (a[ans1-1][i]==b[ans2-1][j]){
               c++;
               rs=a[ans1-1][i];
               }
        fprintf(fp,"Case #%d: ",ri);
        if (c==0) fprintf(fp,"Volunteer cheated!\n");
        if (c==1) fprintf(fp,"%d\n",rs);
        if (c>1) fprintf(fp,"Bad magician!\n");
    }
    return 0;
}
            
             
