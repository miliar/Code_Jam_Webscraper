#include <bits/stdc++.h>
using namespace std;
int main()
{
 // freopen("out.txt","w",stdout);
  int test, cs = 1;
  scanf("%d",&test);
  while(test--){
     int n,temp ;
     long long ans;
     scanf("%d", &n);
     int hit[12] = {0};
     int i = 1 , counter = 0;
     while(counter < 10 && n != 0){
        ans = temp = n*i;
        while(temp){
           int r = temp%10;
           if(hit[r] == 0){
              hit[r] = 1;
              counter++;
           }
           temp/=10;
        }
        i++;
     }
     if(n == 0) printf("Case #%d: INSOMNIA\n", cs++ );
     else
     printf("Case #%d: %lld\n", cs++ , ans);
  }

}
