#include<stdio.h>

char mark[10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti,cnt;
    long long inp,i,tmp;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%lld",&inp);
        if (inp==0)
        {
            printf ("Case #%d: INSOMNIA\n",ti+1);
            continue;
        }
        cnt=0;
        for (i=0;i<10;++i)mark[i]=0;
        for (i=1;i<=1000000;++i)
        {
            tmp = inp*i;
            while(tmp>0)
            {
                if (mark[tmp%10]==0)
                {
                    mark[tmp%10] = 1;
                    cnt++;
                }
                tmp/=10;
            }
            if(cnt==10)break;
        }
        if (cnt==10)printf ("Case #%d: %lld\n",ti+1,inp*i);
        else printf ("Case #%d: INSOMNIA\n",ti+1);
    }
    return 0;
}
