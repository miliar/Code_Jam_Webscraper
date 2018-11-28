#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    double a[2000];
    double b[2000];
    int n;
    int t;
    int c = 1;
    int i;
    int j;
    int t1;
    int t2;
    int k;
    int d;
    
    scanf("%d", &t);
    while(t--) {
               scanf("%d", &n);
               for(i=0; i<n; i++) {
                       scanf("%lf", &a[i]);
               }
               for(i=0; i<n; i++) {
                        scanf("%lf", &b[i]);
               }
               sort(a, a+n);
               sort(b, b+n);
               k = 0;
               j = 0;
               //t2 = 0;
               for(i=0; i<n; i++) {
                        while(j<n) {
                                   if(b[j]>a[i]) {
                                                 k++;
                                                 j++;
                                                 break;
                                   } else {
                                          j++;
                                   }
                        }
               }
               t2 = 0;
               d = 0;
               for(i=n-1; i>=0; i--) {
                         for(j=d; j<n; j++) {
                                  if(a[j]>b[i]) {
                                                t2++;
                                                a[j] = 0;
                                                break;
                                  } else if(j==n-1 && a[j]<b[i]) {
                                         d++;
                                  }
                         }
               }
                                         
                                                
                                  
                          
                        
               printf("Case #%d: %d %d\n", c, t2, n-k);
    }
    //main();
    return 0;
}
                        
                        
