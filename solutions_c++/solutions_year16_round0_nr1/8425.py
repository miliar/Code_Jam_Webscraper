#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("output_large.txt","w",stdout);
    long long int n,test,cas,temp,i,j;
    int ara[15],cnt,x;
    scanf("%lld",&test);
    for(cas=1;cas<=test;cas++)
    {
        for(i=0;i<10;i++)
            ara[i]=0;
            cnt=0;
        scanf("%lld",&n);
     //   printf("n is %lld \n",n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",cas);
            continue;
        }
        for(i=1;cnt<10;i++)
        {
            temp=n*i;
        //    printf("--------------Case #%lld: %lld\n",cas,temp);
            for(;temp>0;){
                x=temp%10;
                temp = temp/10;
                if(ara[x]==0){
                    ara[x]=1;
                    cnt++;
                }
                if(cnt==10)
                {

                    break;
                }

            }
        }
        printf("Case #%lld: %lld\n",cas,n*(i-1));
    }
    return 0;
}
