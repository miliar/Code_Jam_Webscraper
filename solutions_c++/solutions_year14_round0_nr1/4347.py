#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int arr1[5][5],arr2[5][5];
int r1,r2;
int same,ans;
int T,t;

int main()
{
    int i,j;
    freopen("Ain.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&r1);
        for(i=1;i<=4;i++) for(j=1;j<=4;j++) scanf("%d",&arr1[i][j]);
        scanf("%d",&r2);
        for(i=1;i<=4;i++) for(j=1;j<=4;j++) scanf("%d",&arr2[i][j]);
        same=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(arr1[r1][i]==arr2[r2][j])
                {
                    same++;
                    ans=arr1[r1][i];
                }
            }
        }
        printf("Case #%d: ",t);
        if(same<1) printf("Volunteer cheated!\n");
        else
        {
            if(same==1) printf("%d\n",ans);
            else printf("Bad magician!\n");
        }
    }
    return 0;
}
