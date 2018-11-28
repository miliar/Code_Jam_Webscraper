#include<bits/stdc++.h>
using namespace std;
int main()
{
int T ;
scanf("%d",&T);
for(int t=1;t<=T;t++)
        {
           int mask=0,desired=1<<10;
           desired--;
           long long N,res;
           scanf("%lld",&N);
           if(N==0) {printf("Case #%d: INSOMNIA\n",t); continue;}
           else
           {    long long i=1;
                long long temp;

                while(mask!=desired)
                 {
                     temp=N*i;
                     res=temp;
                     int n;
                     while(temp>0) {
                             n=temp%10;
                             mask|=(1<<n);
                             temp/=10; }
                     i++;
                 }

           }
           printf("Case #%d: %lld\n",t,res);
        }
        return(0);
}
