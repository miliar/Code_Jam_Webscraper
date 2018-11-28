#include<cstdio>

int main (){
  int tt;
  int k,c,s;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    scanf("%d %d %d",&k,&c,&s);
    printf("Case #%d:",rr);
    for(int i=1;i<=s;i++){
      printf(" %d",i);
    }
    printf("\n");
  }
  return 0;
}
