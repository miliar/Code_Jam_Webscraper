#include<cstdio>
using namespace std;
int main()
{
    int t,a[4][4],b[4][4],c=0,i,j,x,y,e=0,k=0;
  //  freopen("A-small-attempt1.in","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {

        k++;
        c=0;
        scanf("%d",&x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        scanf("%d",&y);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        }
        if(x<5 && y<5)
        {
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[x-1][i]==b[y-1][j])
                {
                        e=a[x-1][i];
                        c++;
                }
            }
        }
        }

        if(c==1)
        {
            printf("Case #%d: %d\n",k,e);
        }
        else if(c==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        else if(c>1)
        {
            printf("Case #%d: Bad magician!\n",k);
        }

    }
    return 0;
}
