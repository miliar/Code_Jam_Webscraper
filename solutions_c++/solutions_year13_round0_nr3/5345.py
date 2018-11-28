#include<iostream>
#include<math.h>
using namespace std;
int pal(int a)
{
int q,r,b=0;
q=a;
while(q!=0)
{
 r=q%10;
 b=(b*10)+r;
 q=q/10;
} 
if(b==a)
 return 1;
else 
 return 0;
}
int main()
{
float s;
int i,l,u,n,j,c1,c2,c[101];
cin>>n;
i=1;
while(i<=n)
   {
     c[i]=0;
     cin>>l>>u;
     j=l;
     while(j<=u)
     	{
     	  c1=pal(j);
     	  s=sqrt(j);
     	  if(s-(int)s!=0)
     	     c2=0;
     	  else
     	     c2=pal(s);
     	  if(c1==1&&c2==1)
     	   c[i]=c[i]+1;
     	   j++;
     	 }
       i++;
    }
    for(i=1;i<=n;i++)
         cout<<"Case #"<<i<<": "<<c[i]<<"\n";
return 1;
}
