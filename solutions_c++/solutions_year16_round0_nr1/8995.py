#include<stdio.h>
int main()
{
    freopen("A-large.in","r",stdin);

    freopen("A-large.out","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(int j=1;j<=t;++j)
    {
        int n,c;
        scanf("%d",&n);
        if(n!=0)
        {   long long int temp,f;

            int d[10]={0,0,0,0,0,0,0,0,0,0};
            for(int i=1;1;++i)
            {
                c=0;
				temp=n*i;
                f=temp;
                while(temp)
                {
                   long long int p;
                    p=temp%10;
                    d[p]++;
                    temp/=10;
                }
                for(k=0;k<10;++k)
                {
                    if(d[k]>1)
                    d[k]=1;
                }
                for(k=0;k<10;++k)
                {
                    if(d[k]==1)
                        c++;
                }
                if(c==10)
                {
                    printf("Case #%d: %lld\n",j,f);
                    break;
                }
            }

        }
        else
             printf("Case #%d: INSOMNIA\n",j);

    }
    return 0;
}
