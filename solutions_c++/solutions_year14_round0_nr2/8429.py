#include<stdio.h>

int main(int agrc,char*agrv[]){
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    double C,F,X;
    scanf("%lf%lf%lf",&C,&F,&X);
    int cnt=X/C-2/F;
    double res=0;
    for(int i=0;i<cnt;i++)
      res+=C/(2+F*i);
    if(cnt<0) cnt=0;
    res+=X/(2+F*cnt);
    printf("Case #%d: %lf\n",tc,res);
  }
  return 0;
}
