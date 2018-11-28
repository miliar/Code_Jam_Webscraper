using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>

typedef long long int int64;

int main()
{
    int64 t,i,j,k,n,m,l,fl,ans,mx,a[15][15],bi[15],x,y,z,fli,flj;
    
   //freopen("inba.txt","r",stdin);
   //freopen("outbc.txt","w",stdout);
    
    scanf("%lld",&t); 
    for(mx=1; mx<=t; mx++)
    {
     scanf("%lld%lld",&n,&m);
     ans=0; k=0;
     
     for(i=0; i<n; i++) for(j=0; j<m; j++) scanf("%lld",&a[i][j]); 
     
     for(i=0; i<n; i++)
     {
       for(j=0; j<m; j++) 
       {    
          fli = flj=0;   
          if(a[i][j]==1)
          {  
            k++;             
            for(l=0; l<n; l++) if(a[l][j]==1) fli++;
            for(l=0; l<m; l++) if(a[i][l]==1) flj++;
            if(fli==n || flj==m) ans++;
          }
       }    
     }
     
     
    if(ans==k || n==1) printf("Case #%lld: YES\n",mx);
    else printf("Case #%lld: NO\n",mx);
    }
    
    return 0;
}
