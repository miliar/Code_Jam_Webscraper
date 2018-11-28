#include<iostream>
#include<cstdio>
#include<cstring>

#define maxn 20
using namespace std;

int t,x,y;
bool used[maxn];

int main()
{
    freopen("a_2.in","r",stdin);
    freopen("a_2.out","w",stdout);
    cin>>t;
    for (int cas=1;cas<=t;cas++)
    {
        memset(used,0,sizeof(used));
        cin>>x;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
            {
                cin>>y;
                if (i==x)
                    used[y]=true;
            }
        cin>>x;
        int res=0,bj;
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
            {
                cin>>y;
                if (i==x)
                    if (used[y]) res++,bj=y;
            }
        printf("Case #%d: ",cas);
        if (res>1) puts("Bad magician!");
        else if (res==0) puts("Volunteer cheated!");
        else printf("%d\n",bj);
    }
    return 0;
}
