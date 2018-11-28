/*krypto........................jagsxi...!! */
#include<bits/stdc++.h>


long long int gcd(long long int a, long long int b)
{
    if (a%b == 0) 
       return b;
    else return gcd(b,a%b);
       
}
int main()
{
    long long int t;
    long long int p,q,g,copy,k,ans;
    scanf("%lld",&t);
    for (k = 1; k <= t; k++) {
          ans = 0;
          scanf("%lld/%lld",&p,&q);    
          g = gcd(p,q);
          p = p/g;
          q = q/g;
          copy = q;
          while (copy != 0) {
             if (copy % 2 == 1 && copy != 1)
                 break;
             copy = copy/2;    
          }
          if (copy != 0) {
             printf("Case #%lld: impossible\n",k);
             continue;
          }
    
          
              
          while (q > p) {
                q = q/2;
                ans++;
                
          }
          
          printf("Case #%lld: %lld\n",k,ans);
    }
    return 0;
}
          
          
