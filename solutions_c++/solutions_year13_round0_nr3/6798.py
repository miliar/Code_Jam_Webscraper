#include<stdio.h>
#include<math.h>
int t,a,b,i,j=1;
bool isPalindrome(int x) {
  if (x < 0) return false;
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}
bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    return n == root * root;
}
int main()
{
    scanf("%d",&t);
    while(t--)
    {
        int count=0;
        scanf("%d %d",&a,&b);
        for(i=a;i<=b;i++)
        {
            if(isPalindrome(i))
            {
                if(is_perfect_square(i))
                {
                    if(isPalindrome(sqrt(i)))
                    {
                       count++;
                    }
                }
            }
        }
        printf("Case #%d: ",j);
        j++;
        printf("%d",count);
    }
}
