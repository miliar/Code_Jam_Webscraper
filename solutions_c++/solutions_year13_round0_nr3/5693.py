#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
 int t,c;c=1;
freopen("t.in","r",stdin);
freopen("op.txt","w",stdout);
 cin>>t;
 while(t--)
 {
     long n,i,a,b;n=0;
     cin>>a;
     cin>>b;
     cout<<"Case #"<<c++<<": ";
     for(i=a;i<=b;i++)
     {
         long d,rev,tmp;rev=0;tmp=i;
         double s;
         while(tmp!=0)
         {
             d=tmp%10;
             tmp=tmp/10;
             rev=((rev*10)+d);
         }
         if(rev==i)
         {
             s=sqrt(i);
             if(pow(s,2)==i)
             {
                 long tmp2,d2,rev2;
                 tmp2=(long)s;rev2=0;
                 while(tmp2!=0)
         {
             d2=tmp2%10;
             tmp2/=10;
             rev2=((rev2*10)+d2);
         }if(rev2==s)n++;

             }
         }
         }
         cout<<n<<endl;
     }
     return 0;
 }
