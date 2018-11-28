#include<iostream>
#include<cstdio>
#define gc getchar_unlocked

void scanint(long long int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
using namespace std;
int main()
{
   long long int t,t1=1,a,b,k,count;
    scanint(t);
   // cout<<a<<endl;
   while(t--)
   {
       count=0;
       scanint(a);
       scanint(b);
       scanint(k);
       if(k>=a||k>=b)
       {
            count=a*b;
       }
       else if(k<a&&k<b)
       {
           count=(k*b)+((a-k)*k);
            for(long long int i=k;i<a;i++)
            {
               for(long long int j=k;j<b;j++)
               {
                   long long int k1=i&j;
                   //cout<<k1<<endl;
                   if(k1<k)
                        count++;
               }
            }    
       }
       cout<<"Case #"<<t1++<<": "<<count<<endl;
   }
   return 0;
}