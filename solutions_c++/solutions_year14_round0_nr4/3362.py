#include <stdio.h>
#include <algorithm>
#include <string.h>
int check_a[1005], check_b[1005];
double a[1005], b[1005];

int minimum(double y, int n)
{
    double min = 3.0;
    int i, index;
    for (i = 0; i < n; i++) {
        if (check_b[i] == 1 && b[i] - y < min && b[i] - y > 0) {
            min = b[i] - y;
            index = i;
        }
    }
    return index;
}

int minimum1(double y, int n)
{
    double min = 3.0;
    int i, index;
    for (i = 0; i < n; i++) {
        if (check_a[i] == 1 && a[i] - y < min && a[i] - y > 0) {
            min = a[i] - y;
            index = i;
        }
    }
    return index;
}
using namespace std;
int main()
{
    int t, n,  ans1, ans2, x, index,i,j,k, left, right, z;
    
    scanf("%d",&t);
    for (k = 1; k <= t; k++) {
         memset(&check_a[0],0,sizeof(check_a));
         memset(&check_b[0],0,sizeof(check_b));
          ans1 = 0;
          ans2 = 0;
          scanf("%d",&n);
          for (i = 0; i < n; i++) {
              scanf("%lf",&a[i]);
              check_a[i] = 1;
          }
          for (i = 0; i < n; i++) {
              scanf("%lf",&b[i]);
              check_b[i] = 1;
          }
          sort(a,a+n);
          sort(b,b+n);
          
         /* for (i = 0; i < n; i++) {
              if (a[i] > b[i]) {
                  ans1++;
              }
          }
          */
          left = 0;
          right = n - 1;
          for (i = n - 1; i >= 0; i--) {
              if (b[i] > a[right]) {
                  //ans2++;
                  check_a[left] = 0;
                  for (x = 0; x < n; x++) {
                      if (check_a[x] == 1)
                         break;
                  }
                  left = x;
              }
              else if (b[i] < a[right]) {
                   ans1++;
                   z = minimum1(b[i],n);
                   check_a[z] = 0;
                   for (x = n - 1; x >= 0; x--) {
                       if (check_a[x] == 1)
                         break;
                   }
                   right = x;
                   
              }
          }
          
          left = 0;
          right = n - 1;
          for (i = n - 1; i >= 0; i--) {
              if (a[i] > b[right]) {
                  ans2++;
                  check_b[left] = 0;
                  for (x = 0; x < n; x++) {
                      if (check_b[x] == 1)
                         break;
                  }
                  left = x;
              }
              else if (a[i] < b[right]) {
                   z = minimum(a[i],n);
                   check_b[z] = 0;
                   for (x = n - 1; x >= 0; x--) {
                       if (check_b[x] == 1)
                         break;
                   }
                   right = x;
                   
              }
         /*     for (x = 0; x < n; x++) {
                  printf("%d ",check_b[x]);
              }
              printf("\n");
              printf("left = %d   right = %d\n",left,right);
              */
          }
          printf("Case #%d: %d %d\n",k,ans1,ans2);
    }
    return 0;
}
          
          
          
    
    
