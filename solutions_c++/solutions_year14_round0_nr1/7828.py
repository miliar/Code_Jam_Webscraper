#include<stdio.h>
using namespace std;


int a[4][4];

int ans1[4];
int ans2[4];

int main()
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        int i,j,r,c,v;
        scanf("%d",&r);
        r--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        for(i=0;i<4;i++)
            ans1[i]=a[r][i];

        scanf("%d",&r);
        r--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        for(i=0;i<4;i++)
            ans2[i]=a[r][i];

        c=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(ans1[i]==ans2[j])

        {
          c++;
          v=ans1[i];

        }

        if(c==0)
            printf("Case #%d: Volunteer cheated!\n",w);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",w);
        else printf("Case #%d: %d\n",w,v);


    }
}
