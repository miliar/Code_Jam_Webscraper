#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int tc,r1,r2,ar[5][5],ar2[5][5],cnt,ans;

    scanf("%d",&tc);
    for(int t=1; t<=tc; t++)
    {
        scanf("%d",&r1);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&ar[i][j]);
        scanf("%d",&r2);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&ar2[i][j]);

        cnt=0;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                if(ar[r1][i]==ar2[r2][j])
                {
                    ans = ar[r1][i];
                    cnt++;
                    break;
                }

        printf("Case #%d: ",t);
        if(cnt==0) puts("Volunteer cheated!");
        if(cnt==1) printf("%d\n",ans);
        if(cnt>1) puts("Bad magician!");
    }
}
