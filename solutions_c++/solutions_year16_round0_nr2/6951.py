#include<cstdio>
#include<cstring>
#include<cstdlib>
void work()
{
  char s[200];
  scanf("%s", s);
  int res = 0;
  int n = strlen(s);
  for(int i = 1; i<n; i++){
    if (s[i] != s[i-1])
      res++;
  }
  if (s[n-1]=='-')
    res++;
  printf("%d\n",res);
}
int main()
{
  int K;
  scanf("%d",&K);
  for(int i =1; i <=K;i++){
    printf("Case #%d: ",i);
    work();
  }
}
