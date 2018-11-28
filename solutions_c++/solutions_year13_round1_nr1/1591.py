#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
int main()
{
//    freopen("C:\\Users\\wrathchild\\Desktop\\input.txt","r",stdin);
//    freopen("C:\\Users\\wrathchild\\Desktop\\output.txt","w",stdout);
    long long test,temp=0;
    scanf("%lld",&test);
    while(test--)
    {
        temp++;
     long long r,t,count=1,i=5;scanf("%lld",&r);scanf("%lld",&t);
     long long x=2*r;
     t-=(2*r)+1;
     while(1)
     {
         if((t-(i+x))>=0)
         {
             count++;
             t-=(i+x);
             i+=4;
         }
         else
         break;
     }
     printf("Case #%lld: %lld\n",temp,count);

    }
    return 0;
}

