#include<cstdio>
#include<cstring>
char str[105];
int main()
{
  int i, T, len, count, j;
  scanf("%d",&T);
  for (i=1; i<=T; i++) {
    scanf("%s",str);
    len = strlen(str);
    count = 0;
    for (j=1; j<len; j++) {
      if (str[j] != str[j-1]) {
	count++;
      }
    }
    if (count%2==0 && str[0]=='-') {
      count++;
    }
    if (count%2==1 && str[0]=='+') {
      count++;
    }
    printf("Case #%d: %d\n", i, count);
  }
  return 0;
}
