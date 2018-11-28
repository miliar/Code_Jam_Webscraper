#include<cstdio>
#include<algorithm>
using namespace std;

int num[5];

int main()
{
    int t,n;
    int ca=1;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        n--;
        for(int i=0; i<4; i++)
        {
            if(i==n)
            {
                for(int j=0; j<4; j++)
                    scanf("%d",&num[j]);
            }
            else
            {
                for(int j=0; j<4; j++)
                    scanf("%d",&num[4]);
            }
        }
        scanf("%d",&n);
        n--;
        int ans=0,ret=0;
        for(int i=0; i<4; i++)
        {
            if(i==n)
            {
                for(int k=0; k<4; k++)
                {
                    scanf("%d",&num[4]);
                    for(int j=0; j<4; j++)
                        if(num[4]==num[j])
                        {
                            ans++;
                            ret=num[4];
                        }
                }
            }
            else
            {
                for(int j=0; j<4; j++)
                    scanf("%d",&num[4]);
            }
        }
        printf("Case #%d: ",ca++);
        if(ans==1)
            printf("%d\n",ret);
        else if(ans==0)
            puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
    return 0;
}
