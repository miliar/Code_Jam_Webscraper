#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a[4][4],b[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,tt=0,i,j,r1,r2,cnt,tmp;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        scanf("%d",&r1);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&r2);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        cnt=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a[r1-1][i]==b[r2-1][j])
                {
                    tmp=a[r1-1][i];
                    cnt++;
                }
        printf("Case #%d: ",tt);
        if(cnt>1)puts("Bad magician!");
        else if(cnt==1)printf("%d\n",tmp);
        else puts("Volunteer cheated!");
    }
    return 0;
}
