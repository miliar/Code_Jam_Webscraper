#include<iostream>
#include<math.h>
using namespace std;
int temp,r,n,p,i,answer;
int checkpal(int n)
{ 
  temp=p;
  r=0;
  while(temp>0)
    {
               r=r*10;
               r=r+temp%10;
               temp=temp/10;
    } 
   if(p==r)
   answer++;
}
int check(int n)
{ 
  float num;
  r=0;  
  temp=n;
  while(temp>0)
    {
               r=r*10;
               r=r+temp%10;
               temp=temp/10;
    } 
   if(n==r)
   {
      num=sqrt(r);
      p=num;
      if(p==num)
        {
           checkpal(p);
        }
   }
}
int main()
{
    freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
   int test,a,b,x=1;
   cin>>test;
   while(test--)
   {   answer=0;
       cin>>a>>b;
       for(i=a;i<b+1;i++)
       {
       check(i);
       }
       cout<<"Case #"<<x<<": "<<answer<<endl;
       x++;
   }   
}
