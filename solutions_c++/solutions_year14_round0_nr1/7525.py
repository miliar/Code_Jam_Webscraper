#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int a,b;
    int data[5][5],data2[5][5];
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&data[i][j]);
            }
        }
        scanf("%d",&b);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&data2[i][j]);
            }
        }
        int s=0,ans;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(data[a][i]==data2[b][j])
                {
                    s++;
                    ans=data[a][i];
                    break;
                }
            }
        }
        if(s==1)
        {
            printf("Case #%d: %d\n",t,ans);
        }
        else if(s==0)
        {
            printf("Case #%d: Volunteer cheated!\n",t);
        }
        else printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}

