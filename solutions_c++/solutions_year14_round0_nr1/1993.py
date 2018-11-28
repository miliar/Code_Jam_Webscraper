#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "rt", stdin);
    freopen("A-small0.out", "wt", stdout);
    int r1,r2,a[5][5],b[5][5],i,j,temp,t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int check[5]={0};
        cin>>r1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            cin>>a[i][j];
        cin>>r2;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            cin>>b[i][j];

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(b[r2][i]==a[r1][j])
                {
                    check[i]=1;
                    break;
                }
            }
        }
        int cnt1=0,cnt0=0;
        for(i=1;i<=4;i++)
            if(check[i])
            cnt1++;
            else
                cnt0++;
        if(cnt0==4)
        {printf("Case #%d: Volunteer cheated!\n",k);continue;}
        else if(cnt1>1)
        {
            printf("Case #%d: Bad magician!\n",k);continue;
        }
        else if(cnt1==1)
        {
            for(i=1;i<=4;i++)
                if(check[i]==1)
                temp=i;

            printf("Case #%d: %d\n",k,b[r2][temp]);continue;
        }
    }
    return 0;
}
