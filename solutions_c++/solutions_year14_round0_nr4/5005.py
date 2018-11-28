#include<stdio.h>
#include <algorithm>

using namespace std;
int main()
{
    int n,i,l,j;
    
    int cases;
    scanf("%d",&cases);
    for(l = 1;l <= cases;l++){
    scanf("%d",&n);
    int value;
    double na[n+1];
    double k[n+1];
    for(i = 0;i < n;i++){
          scanf("%lf",&na[i]);
    }
    for(i = 0;i < n;i++){
          scanf("%lf",&k[i]);
    }
    sort(na,n);
    sort(k,n);
    
    i = n-1;
    j = n-1;
    int c = 0;
    while(i >= 0 && j >= 0){
            if(na[j] >= k[i]) {
                     c++;
                     j--;
                     i--;
            }else i--;
    }
    i = n-1;
    j = n-1;
    int c1 = 0;
    while(i >= 0 && j >= 0){
            if(na[j] >= k[i]) {
                     j--;
                     c1++;
            }else {
                  i--;
                  j--;
            }
    }
    printf("Case #%d: %d %d\n",l,c,c1);
}
    
    return 0;
}
