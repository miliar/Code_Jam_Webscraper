#include<stdio.h>
int main(){
    freopen("C:\\Users\\WAhid\\Desktop\\D-small-attempt2.in","r",stdin);
    freopen("C:\\Users\\WAhid\\Desktop\\output.txt","w",stdout);
int x,r,c,t,cas=0,i,a[5][5][5],j;
for(i=1;i<=4;i++){
    for(j=1;j<=4;j++){
        a[1][i][j]=2;
        a[2][i][j]=2;
        a[3][i][j]=1;
        a[4][i][j]=1;
    }
}
a[2][1][1]=1;
a[2][1][3]=1;
a[2][3][1]=1;
a[2][3][3]=1;

a[3][2][3]=2;
a[3][3][2]=2;
a[3][3][3]=2;
a[3][3][4]=2;
a[3][4][3]=2;

a[4][3][4]=2;
a[4][4][3]=2;
a[4][4][4]=2;


scanf("%d",&t);
while(t--){
    scanf("%d%d%d",&x,&r,&c);
    if(a[x][r][c]==1){
        printf("Case #%d: RICHARD\n",++cas);
    }
    else
        printf("Case #%d: GABRIEL\n",++cas);

}
}

