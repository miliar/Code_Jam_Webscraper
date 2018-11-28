#include<iostream>
using namespace std;
int main()
{
long long int a[10],h,i,j,n,k=1,s=0,t,b,bb,r;
for(j=0;j<10;j++)
  a[j]=0;
cin>>t;
while(t--)
 {s=0;
 cin>>n;
 for(j=0;j<10;j++)
  a[j]=0;
 if(n!=0)
 {
 i=1;
 s=0;
 while(s!=10)
   {s=0;
     b=n*i;
     i++;
     h=bb=b;
     while(b)
       {
       r=b%10;
       a[r]=1;
       b=b/10;
       }
     for(j=0;j<10;j++)
        {
         s=s+a[j];
       }
   }
   //cout<<s;
  cout<<"Case #"<<k<<": "<<h<<"\n";
 }
 else
   cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
   k++;
 }
 
return 0;
}