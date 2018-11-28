#include<stdio.h>
using namespace std;
bool is_pallindrome(long long num)
{
    long long first=num,rev=0;
    
    while(num){
                rev*=10;
               rev+=num%10;
               num/=10;
              
               }
               if(rev==first)return true;
               return false;
}
int between(long long a,long long b,long long c)
{
    if(c<a)return 0;
    if(c>b)return 0;
    return 1;
}
 long long fair[10000005];
int main()
{
 int t;
 int count=0;
 
 long long m,a,b,hi=10000000;
 for(m=1;m<=hi;m++)
 {long long square = m*m;
                   if(is_pallindrome(m) && is_pallindrome(square))fair[count++] = square;
                   }
                  
 scanf("%d",&t);

 int i;
 for(i=0;i<t;i++)
 {
                 long long ans=0;
                 
                 scanf("%lld%lld",&a,&b);
                 int j;
               for(j=0;j<count;j++)
               if(between(a,b,fair[j]))ans++;
                 
                 printf("Case #%d: %lld\n",i+1,ans);
                 }
 
    
}
