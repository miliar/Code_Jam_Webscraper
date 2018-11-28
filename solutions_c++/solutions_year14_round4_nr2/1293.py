#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

long long t, tt, i,j,k,l,n,m,h;
long long a[100],b[100],v[100];
vector<long long> lavy, pravy;
map<long long, long long> inverz;


long long makaj()
{
long long ii,jj,vv;

vv = 0;

for(ii=0;ii<n;ii++)
 for(jj=ii+1;jj<n;jj++)
   if(inverz[a[ii]] > inverz[a[jj]]) vv++;
 
return vv;
}


int main()
{

scanf("%lld",&t);

for(tt=1;tt<=t;tt++)
{
  scanf("%lld",&n);
  
  for(i=0;i<n;i++) scanf("%lld",a+i);

  k = a[0];

  for(i=0;i<n;i++) if(a[i] > k) k = a[i];

  j = 0;
  for(i=0;i<n;i++)
   if(a[i] != k) 
     {
     b[j] = a[i];
     j++;
     }


h = 100000000;
     

   for(m=0;m< (1<<(n-1));m++)
    {
     lavy.clear();
     pravy.clear();
    
     for(j=0;j<n-1;j++) if(m & (1<<j)) lavy.push_back(b[j]);
                        else pravy.push_back(b[j]);
   
     sort(lavy.begin(), lavy.end());
     sort(pravy.begin(), pravy.end()); 
   
     i = 0;
     
     for(j=0;j< lavy.size(); j++) {v[i] = lavy[j]; i++;}
     
     v[i] = k;
     i++;
     
     if(pravy.size()>0) for(j=pravy.size()-1;j>=0;j--) {v[i] = pravy[j];i++;}
    
     inverz.clear(); 
    
     for(i=0;i<n;i++) inverz[v[i]] = i;
    
//    return 0;
        
     
     if(makaj() < h) h = makaj();
    
//     for(i=0;i<n;i++) printf("%lld ",v[i]); 
//     printf("%lld \n",h);    
    }

printf("Case #%lld: %lld\n",tt,h);

}



return 0;
}