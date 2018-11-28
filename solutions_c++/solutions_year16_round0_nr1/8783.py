#include<bits/stdc++.h>

using namespace std;
int main()

{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int t,j,cnt;
  scanf("%d",&t);


  for(j=1;j<=t;j++)

     {
         int v[]={0,0,0,0,0,0,0,0,0,0};

         long long int n;
         long long int k;

         int i=1;

         scanf("%lld",&n);

         if(n==0)
         printf("Case #%d: INSOMNIA\n",j);
         else
        {
              while(1)
              {

                    k=n*i;
                    cnt=0;
                    long long int tmp=k;
                    while(tmp)
                        {
                           int a=tmp%10;
                           v[a]++;
                           tmp/=10;
                        }
                    for(int b=0;b<10;b++)
                        {
                           if(v[b]>=1)
                           cnt++;
                        }

                    if(cnt==10)
                       {
                         printf("Case #%d: %lld\n",j,k);
                         break;
                       }
                    i++;
                }
         }

     }
  return 0;
}

