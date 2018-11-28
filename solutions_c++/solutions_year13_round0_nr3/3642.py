#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_MN 100


unsigned long long int a,b;
unsigned long long int ra,rb;

int d[100];

bool ispalindrome(unsigned long long int  a) {
  int i;
  i = 0;
  while (a > 0) {
    d[i++] = a % 10;
    a = a / 10;
  }

  int h = 0;
  i--;
  while (h < i) {
    if (d[h] != d[i]) return false;
    h++;
    i--;
  }
  return true;

}


int main()
{
  freopen("C-small-attempt0.in","r",stdin);
  int T;
  scanf("%d\n",&T);

  //if (ispalindrome(122222222222223L)) printf("YES\n");
  //exit(0);
  for (int CASE = 1;CASE <= T;CASE++) {
    scanf("%llu %llu",&a,&b);
    int count;
    count = 0;

    ra = ceil(sqrt(a));
    rb = sqrt(b);

    for (unsigned long long int i = ra;i <= rb;i++) {
      //printf("checking %llu\n",i);
      if (ispalindrome(i)) {
        //printf("%llu is palin\n",i);
        if (ispalindrome(i*i)) {
          //printf("%llu is palin\n",i*i);
          count++;
        }
      }
    }
    printf("Case #%d: %d\n",CASE,count);

  }
}
