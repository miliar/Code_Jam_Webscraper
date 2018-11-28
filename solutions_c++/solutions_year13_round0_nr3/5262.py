#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int T,A,B,Case;
double a[1002];
int hui(int i)
{
  int flag=0;
  int t=i,j;
  if(t<10) {flag=1;return flag;}
  int c[100];
  int n=0;
  while(t)
  {
    c[++n]=t%10;
    t/=10;        
  } 
   for(j=1;j<=n/2;j++)
   {
     if(c[j]!=c[n+1-j]) break;       
   }  
   if(j>n/2) flag=1;
   return flag; 
}
int main()
{
   freopen("3.in","r",stdin);
   freopen("3.out","w",stdout);
   cin>>T;
   Case=0;
   memset(a,0,sizeof(a));
   for(int i=1;i<=1001;i++)
     {
       double b=sqrt(double(i));
       if(i==b*b) a[i]=1;      
     } 
   for(int i=1;i<=1001;i++)
   {
       if(!a[i]) continue;
       if(!hui(i)) a[i]=0; 
        //else cout<<i<<endl;        
   }
       
   while(T--)
   {
     int ans=0;
     cin>>A>>B;
     for(int i=A;i<=B;i++)
       {
         if(a[i]) 
         {
           if(hui(sqrt(double(i)))) ans++;        
         }    
       } 
       cout<<"Case #"<<++Case<<": "<<ans<<endl;        
   } 
}
