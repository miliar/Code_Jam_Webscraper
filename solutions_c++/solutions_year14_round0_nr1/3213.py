#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int mp[20];

int main()
{
    int tes;
    int i,j;

    //freopen("abc.in","r",stdin);
    freopen("abc.txt","w",stdout);
    cin>>tes;

    for(int cas=1;cas<=tes;cas++)
    {
        memset(mp,0,sizeof(mp));
        int n,t;

        int ca=2;
        while(ca--)
        {
            cin>>n;
            for(i=1; i<=4; i++)
            {
                for(j=1; j<=4; j++)
                {
                    cin>>t;
                    if(i==n)
                        mp[t]++;
                }
            }
        }

        int q=0;
        for(i=1;i<=16;i++)
            if(mp[i]==2)
                q++;
        printf("Case #%d: ",cas);
        if(q>1) puts("Bad magician!");
        else if(q==0) puts("Volunteer cheated!");
        else
        {
            int p;
            for(i=1;i<=16;i++)
            {
                if(mp[i]==2)
                {
                    p=i;
                    break;
                }
            }
            printf("%d\n",p);
        }
    }
    return 0;
}
