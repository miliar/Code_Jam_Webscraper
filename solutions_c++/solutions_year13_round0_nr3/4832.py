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

int64 sa[10000011]; 
void squarea()
{
    int64 i;
    for(i=1; i<=10000000; i++) {sa[i] = i*i;}
}

int found(int64 n)
{
    int64 i,j,fl=0;
    for(i=1; ;i++)
    {
             if(sa[i]>n) break;
             if(sa[i]==n) return i;     
    }
    return -1;
}

int check(int64 n)
{
    int64 i,j,k,n1,n2,dg[15];
    
    n1=n; n2=0; k=1; i=0;
    while(n1>0)
    {
           j=n1%10;
           dg[i] = j;
           n1/=10;  
           i++; k*=10;
    }    
    
    for(j=0; j<i; j++)
    { k/=10; n2+= dg[j]*k; }
    //cout<<n<<" "<<n2<<endl;
    
    if(n==n2) return 1;
    else return 0;
}

int main()
{
    int64 t,i,j,k,n,m,ans,mx,a,b,x,y,z,fli,flj;
    char st[211];
    //freopen("inc.txt","r",stdin);
    //freopen("outc.txt","w",stdout);
    squarea();
    scanf("%lld",&t); 
    for(mx=1; mx<=t; mx++)
    {
     scanf("%lld%lld",&a,&b);
     ans=0;
     for(i=a; i<=b; i++)
     {
            if(check(i)==1)
            {
                   k =found(i);        
                   if(k>0)
                   {
                      if(check(k)==1)    ans++;
                   } 
            }
     }
     
    printf("Case #%lld: %lld\n",mx,ans);
    }
    
    return 0;
}
