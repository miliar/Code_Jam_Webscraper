#include <iostream>
#include <cstdio>
using namespace std;
unsigned int a[4][4],b[4][4];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    unsigned int t;
    scanf("%d",&t);
    for(unsigned int k=1;k<=t;k++)
    {
        unsigned int ax,bx;
        scanf("%d",&ax);
        ax--;
        for(unsigned int i=0;i<4;i++)
        {
            for(unsigned int j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        scanf("%d",&bx);
        bx--;
        for(unsigned int i=0;i<4;i++)
        {
            for(unsigned int j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        }
        unsigned int c=0,lo=0;
        for(unsigned int i=0;i<4;i++)
        {
            for(unsigned int j=0;j<4;j++)
            {
                if(b[bx][j]==a[ax][i])
                {
                    c++;
                    lo=b[bx][j];
                    break;
                }
            }
        }
        printf("Case #%d: ",k);
        if(c==1)
            printf("%d\n",lo);
        else if(c==0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
