#include<cstdio>
int cnt[11];
int main()
{
    long long int n,tmp;
    int t,chk;
    scanf("%d",&t);
    for(int testcase=1;testcase<=t;++testcase)
    {
        for(int i=0;i<10;i++) cnt[i]=0;
        scanf("%lld",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",testcase);
        else
        {
            long long int p=1;
           while(1)
            {
                chk=0;
                tmp=n*p;
                while(tmp)
                {
                    cnt[tmp%10]=1;
                    tmp/=10;
                }
                for(int j=0;j<=9;j++)
                {
                    if(cnt[j]==0) chk=1;
                }
                if(chk==0)
                {
                    printf("Case #%d: %lld\n",testcase,n*p);
                    break;
                }
                p++;
            }
       
        }
    }
    return 0;
}