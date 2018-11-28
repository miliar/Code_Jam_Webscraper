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

typedef long long int int64;

int main()
{
    int64 test,t,i,j,k,n,r,ans,sum,fill;
    
    
    //freopen("inl.txt","r",stdin);
    //freopen("outl.txt","w",stdout);
    
    cin>>test;
    
    for(i=1; i<=test; i++)
    {
     scanf("%lld %lld",&r,&t);
     
       sum=ans=0;
       for(j=1;;j+=2)
       {   
           k = j-1; 
           //fill =  ((r+j)*(r+j))-((r+k)*(r+k)); 
           fill = 2*r+2*j-1;        
           if((sum+fill)>t) break;     
                
           sum += fill;
           //printf("%lld:",sum);
       } 
         
    ans=j/2;
    printf("Case #%lld: %lld\n",i,ans);
    }
    return 0;
}
