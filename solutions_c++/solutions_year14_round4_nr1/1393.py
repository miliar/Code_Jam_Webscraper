#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<long long> a;
long long x,t, tt, i,j,k,l,m,n;

int main()
{

scanf("%lld",&t);

for(tt=1;tt<=t;tt++)
{
a.clear();

scanf("%lld %lld", &n, &x);

for(i=0;i<n;i++) 
  {
   scanf("%lld", &k);
   a.push_back(k);  
  }


sort(a.begin(), a.end());

l = 0;

i = 0;
j = n-1;


while(j>=i)
 {
   l++;
   if(a[j] + a[i] <= x) i++;
   j--; 
 }
 

printf("Case #%lld: %lld\n",tt,l);
}


return 0;
}