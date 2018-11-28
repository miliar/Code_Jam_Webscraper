#include<stdio.h>
#include<string.h>
int a[4][4];
int b[4][4];
int count[17];
int main ()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out","w",stdout);
    int T,x,y,ans,show;
    scanf("%d",&T);
    for(int icase=1;icase<=T;icase++){
        scanf("%d",&x);
        x--;
        for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
        scanf("%d",&a[i][j]);
        }}
        scanf("%d",&y);
        y--;
        for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
        scanf("%d",&b[i][j]);
        }}
        
        memset(count,0,sizeof(count));
        for(int j=0;j<4;j++)
        {
            count[a[x][j]]++;
            count[b[y][j]]++;
        }
        ans =0;
        for(int i=1;i<=16;i++)
        {
            
            if(count[i]>=2){
                ans++;
                show =i;
            }
        }
        printf("Case #%d: ",icase);
        if(ans>=2){
            printf("Bad magician!\n");
        }else if(ans==0){
            printf("Volunteer cheated!\n");
        }else{
            printf("%d\n",show);
        } 
    }
    return 0;
}
