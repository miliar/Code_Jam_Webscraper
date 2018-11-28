#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;

int main()
{
    int T,j;
    cin>>T;
    for(j=1;j<=T;j++)
    {
        int a[4][4],b[4][4];
        int pre,now;
        cin>>pre;
        pre--;
        for(int i=0;i<4;i++)
        {
            scanf("%d %d %d %d",&a[i][0],&a[i][1],&a[i][2],&a[i][3]);
        }
        cin>>now;
        now--;
        for(int i=0;i<4;i++)
        {
            scanf("%d %d %d %d",&b[i][0],&b[i][1],&b[i][2],&b[i][3]);
        }
        int sum = 0,ansi;
        for(int i=0;i<4;i++)
            for(int k=0;k<4;k++)
        {
            if(a[pre][i]==b[now][k])
            {
                sum++;
                ansi = i;
            }
        }
        if(sum==1)
        {
            printf("Case #%d: %d\n",j,a[pre][ansi]);
        }
        else if(sum==0)
        {
            printf("Case #%d: Volunteer cheated!\n",j);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",j);
        }
    }
    return 0;
}
