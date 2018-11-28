#include<cstdio>
using namespace std;
int main()
{

    int t,a[10][10],b[10][10],d,i,j,n1,n2,c[20],cnt,cse=1;
    //freopen("C:\\Users\\Anunay\\Desktop\\input.txt","r",stdin);
 //   freopen("C:\\Users\\Anunay\\Desktop\\output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        cnt=0;
        for(i=0;i<20;i++)
            c[i]=0;
        scanf("%d",&n1);

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&n2);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
                if(n2-1==i)
                    c[b[i][j]]=1;
            }
        for(i=0;i<4;i++)
        {
            if(c[a[n1-1][i]]==1)
            {
                cnt++;
                d=a[n1-1][i];
            }
        }
        if(cnt==1)
            printf("Case #%d: %d\n",cse,d);
        else if(cnt==2 || cnt == 3 || cnt ==4)
            printf("Case #%d: Bad magician!\n",cse);
        else
            printf("Case #%d: Volunteer cheated!\n",cse);
        cse++;
    }
    return 0;
}
