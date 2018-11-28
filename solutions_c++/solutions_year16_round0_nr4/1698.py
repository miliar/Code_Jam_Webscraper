#include<cstdio>
int main()
{
  int i, j, T, K, C, S;
  scanf("%d", &T);
  for (i=1; i<=T; i++) {
    scanf("%d %d %d",&K,&C,&S);
    printf("Case #%d: ",i);
    for(j=1; j<=K; j++) {
      printf("%d ",j);
    }
    printf("\n");
  }
  return 0;
}
