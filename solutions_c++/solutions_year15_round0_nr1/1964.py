#include <bits/stdc++.h>
using namespace std;

char s[1105];
int t, n, br, sum, len;

int main()
{
  //freopen("t.in", "r", stdin);
  //freopen("t.out", "w", stdout);
  scanf("%d", &t);
  int fff = 0;

   while (t--){
    fff ++;
    scanf("%d%s", &len, &s);

    br = 0;
    sum = s[0] - '0';

     for (int i=1; i<=len; i++){
       if (sum < i) {
        br++;
        sum++;
       }
       sum = sum + (s[i] - '0');
     }

     printf("Case #%d: %d\n", fff, br);
   }
}
