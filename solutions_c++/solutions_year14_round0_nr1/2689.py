#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[17];

int main()
{
    freopen("A-small-attempt7.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
        int t;
        memset(a,0,sizeof a);

        scanf("%d",&t);
       // printf("%d\n",t);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==t-1) a[x]++;
               // printf("%d ",x);
            }
           // puts("");
        }

        scanf("%d",&t);
       // printf("%d\n",t);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==t-1) a[x]++;
               // printf("%d ",x);
            }
            //puts("");
        }

        int cnt=0,k;
        for(int i=1;i<17;i++) if(a[i]>1) cnt++,k=i;
        printf("Case #%d: ",ca);
        if(cnt==1) printf("%d\n",k);
        else if(cnt>1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
