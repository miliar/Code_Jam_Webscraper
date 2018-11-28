#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[20];

int main()
{
    int T;
    scanf("%d",&T);

    for(int cas=1;cas<=T;cas++)
    {
        int t;
        memset(a,0,sizeof a);

        scanf("%d",&t);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==t-1) a[x]++;
            }
        }

        scanf("%d",&t);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==t-1) a[x]++;
            }
        }

        int cnt=0,k;
        for(int i=1;i<17;i++) if(a[i]>1) cnt++,k=i;
        printf("Case #%d: ",cas);
        if(cnt==1) printf("%d\n",k);
        else if(cnt>1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
