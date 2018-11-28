#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int t, n, ans, count, i, j = 1;
    string s;
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    while (t--) {
          cin>>n;
          cin>>s;
          int l = s.size();
          count = 0;
          ans = 0;
          for (i = 0; i < l; i++) {
              if (count < i) {
                 ans = ans + i - count;
                 count = count + i - count;
              }
              count = count + s[i] - '0';
          }
          printf("Case #%d: %d\n",j++,ans);
    }
    return 0;
    
}


