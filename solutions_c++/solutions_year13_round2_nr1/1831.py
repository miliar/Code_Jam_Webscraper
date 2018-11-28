#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
using namespace std;

int mi(int a,int b,int c)
    {
      if(a<=b && a<=c)
      return a;
      if(b<=a && b<=c)
             return b;
      return c;
             
     }
long long int a[1000];
int n;
int func(long long int size,int pos)
{

 if(pos<(n))
 {if(a[pos]<size)
                  {size+=a[pos];
                   
                   return func(size,pos+1);
                  }
else
    {//cout<<a[pos];
     int dum;
     if((size-1)==0)
     dum=n-pos;
     else
     dum=1+func((2*size-1),pos);
     
     int dum1=dum;
     return mi(dum,dum1,n-pos);
     
    }
}
 return 0;
}

int main()
{
int t;
scanf("%d",&t);
int ca=0;
while(t--)
          {
          ca++;
          int si;
           scanf("%d %d",&si,&n);
          
          for(int i=0;i<n;i++)
                  {
                  scanf("%lld",&a[i]);
                  }
          sort(a,a+n);
          int answer=func(si,0);
          printf("Case #%d: %d\n",ca,answer);
         
          }
}
