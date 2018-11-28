#include<iostream>
using namespace std;

int abs(float a)
{
 if(a<0)
  a=-a;
 return (int)a;
}

int sqrt(int a)
{
 const double EPSILON = 1E-14;
 float xnew = a;
 float xold;
 do 
 { 
  xold = xnew; 
  xnew = (xold + a / xold) / 2; 
 }while (abs(xnew - xold) > EPSILON);
 return (int)xnew;
}

int palin(int p)
{
 int a[4];
 int n=0;
 for(n=0;p!=0;n++)
 {
  a[n]=p%10;
  p/=10;
 }
 int j=n-1;
 for(n=0;n<=j;n++,j--)
 {
  if(a[n]==a[j])
  {
  }
  else 
  {
   return 0;
  }
 }
 return 1;
}
   

int main()
{
 int t,a,b,i;
 int ans[100];
 cin>>t;
 if(t>=1&&t<=100)
 {
  for(i=0;i<t;i++)
  {
   cin>>a>>b;
   ans[i]=0;
   if(a>=1&&b>=1&&a<=1000&&b<=1000)
   {
    for(;a<=b;a++)
	{
	 int sq=sqrt(a);
	 if(sq*sq!=a)
	  continue;
	 if(palin(a))
	 {
	  if(palin(sq))
	  {
	   ans[i]+=1;
	  }
	 }
	}
   }
  }
  for(i=0;i<t;i++)
  {
   cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
  }
 }	     
 return 0;
}

