#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a1[10][10],a2[10][10],b1[10],b2[10];
int main()
{
    freopen("intput.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,h,i,j,x1,x2;
    scanf("%d",&T);
    int k=0;
    while(T--)
    {

        int ans=0;
        scanf("%d",&x1);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a1[i][j]);
        scanf("%d",&x2);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a2[i][j]);
        for(j=1;j<=4;j++)
        {
            b1[j]=a1[x1][j];
            b2[j]=a2[x2][j];
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(b1[i]==b2[j])
                {
                    h=b1[i];
                    ans++;
                }
            }
        }
        printf("Case #%d: ",++k);
        if(ans==0)
        printf("Volunteer cheated!\n");
        else if(ans==1)
        printf("%d\n",h);
        else
        printf("Bad magician!\n");
    }
    return 0;
}
