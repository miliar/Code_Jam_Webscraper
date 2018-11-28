#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

char buf[1024];
char palindrome[1024];

bool is_palindrome(int num)
{
  sprintf(palindrome, "%d",num);
  int n = strlen(palindrome);
  for (int i=0; i<=n/2+1; i++)
    if (palindrome[i] != palindrome[n-i-1])
      return false;
  return true;
}

int valid(int num, int A, int B)
{
  //  printf("checking %d\n",num);
  if (!is_palindrome(num))
    return 0;
  int sq = num*num;
  if (!is_palindrome(sq))
    return 0;
  if (sq >= A && sq <= B)
    return 1;
  return 0;
}

int calc(int A, int B)
{
  int res = 0;
  int a = (int)sqrt(A);
  int b = (int)sqrt(B);
  //  printf("first palindrome betweend %d and %d\n",a,b);

  sprintf(buf,"%d",b);
  int n = strlen(buf);
  buf[n/2] = 0;
  int max = atoi(buf);
  //  printf("max number for first palindrome's left half is %d\n",max);
  
  int upl = (b > 9 ? 9 : b);
  for (int i=a; i<=upl; i++)
    res += valid(i, A, B);

  for (int i=1; i<=max; i++) {
    sprintf(buf,"%d",i);
    int n = strlen(buf);
    buf[2*n] = 0;
    for (int i=0; i<n; i++)
      buf[2*n-i-1] = buf[i];
    res += valid(atoi(buf),A,B);
    for (int i=0; i<n; i++)
      buf[2*n-i] = buf[i];
    buf[2*n+1] = 0;
    for (int i='0'; i<='9'; i++) {
      buf[n] = i;
      res += valid(atoi(buf),A,B);
    }
  }
  return res;
}

int main()
{
  int t;
  scanf("%d",&t);
  for (int tc=1; tc<=t; tc++) {
    int a,b;
    scanf("%d%d",&a,&b);
    printf("Case #%d: %d\n",tc,calc(a,b));
  }
    
  
}
