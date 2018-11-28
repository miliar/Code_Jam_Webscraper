#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main(void)
{
    freopen("A.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int T;
    int N;
    int tt;
    int mask[12];
    scanf("%d",&T);
    int i;
    for(tt=1;tt<=T;tt++)
    {
        scanf("%d",&N);
        memset(mask,0,sizeof(mask));
        int y = 0;

        if(N!=0)
        {

            int tmp = N;
            while(tmp!=0)
            {
                mask[tmp%10] = 1;
                tmp/=10;

            }
            y = 1;
            for(i=0;i<=9;i++)
                if(mask[i]==0)
                    y = 0;
            int nn = N;
            while(y==0)
            {
                N +=nn;

                tmp = N;
                while(tmp!=0)
                {
                    mask[tmp%10] = 1;
                    tmp/=10;

                }
                y = 1;
                for(i=0;i<=9;i++)
                if(mask[i]==0)
                    y = 0;

            }
        }
        if(N==0)
            printf("Case #%d: INSOMNIA\n",tt);
        else
            printf("Case #%d: %d\n",tt,N);
    }


    return 0;
}
