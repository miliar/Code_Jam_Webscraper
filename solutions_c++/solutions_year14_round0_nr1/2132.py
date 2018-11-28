#include<cstdio>
main(){
  int T,a[4][4],x,b[4][4],y;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    scanf("%d",&x);
    --x;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&a[i][j]);
    scanf("%d",&y);
    --y;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&b[i][j]);
    printf("Case #%d: ",t);
    int cnt=0,ans;
    for(int xx=0;xx<4;xx++)for(int yy=0;yy<4;yy++)if(a[x][xx]==b[y][yy]){
      ++cnt;
//      printf("%d %d %d\n",xx,yy,a[x][xx]);
      ans=a[x][xx];
    }
    if(cnt==1)printf("%d\n",ans);
    if(cnt>1)printf("Bad magician!\n");
    if(cnt==0)printf("Volunteer cheated!\n");
  }
}
