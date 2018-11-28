#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
#define constant 32769;
long long int t;
long long int a[11],b[11];
unsigned int n=32769;
int cnt=0,flag=0;
long long int x,y;

int prime()
{flag=0;
for(long long int i=2;i<11;i++)
{
 for(long long int j=2;j<(long long int)floor(sqrt(a[i]));j++)
 {
  if(a[i]%j==0){b[i]=j;j=a[i];flag=1;}
 }
 if(flag!=1)return 0;
 else flag=0;
}
for(int i=0;i<16;i++)
printf("%c",'0'+(int)((n>>15-i)&1));
printf(" %lld %lld %lld %lld %lld %lld %lld %lld %lld\n",b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10]);
cnt++;
if(cnt>=y)exit(0);
return 0;
}
int main()
{
    scanf("%lld",&t);
   while(t--)
    {
    scanf("%lld",&x);

    scanf("%lld",&y);
    printf("Case #%lld: \n",t+1);
     for(int i=0;i<11;i++)
     a[i]=0;

      for(int i=0;i<16384;i++)
      {
        for(int j=2;j<11;j++)
        {
         for(int k=0;k<16;k++)
          {
           a[j]+=(unsigned long long int)((n>>k)&1) * pow(j,k);
           }
        }

         prime();

        for(int i=0;i<11;i++)a[i]=0;
         n+=2;
 }
}


    return 0;
}
