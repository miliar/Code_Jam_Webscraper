#include<cstdio>
#include<vector>

using namespace std;

int main()
{
    int t,n1,n2,tcase=1;
    //freopen("in.txt","r",stdin);
    //freopen("Osman.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        int magic[4][4];
        int flag[20]={0};
        int count=0;
        int ans;
        scanf("%d",&n1);
        for(int i=0;i<4;i++)
        {

            for(int j=0;j<4;j++)
            {
                scanf("%d",&magic[i][j]);
                if(i==n1-1)
                    flag[magic[i][j]]=1;
            }
        }
        scanf("%d",&n2);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&magic[i][j]);
                if(i==n2-1)
                {
                    if(flag[magic[i][j]]==1)
                        count++,ans=magic[i][j];
                }

            }
        }
        printf("Case #%d: ",tcase++);
        if(count==1) printf("%d\n",ans);
        else if(count==0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}

