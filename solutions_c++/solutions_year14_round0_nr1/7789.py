#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t, a[4][4], tmp[4];
    scanf("%d",&t);

    for(int caseno=1; caseno<=t; caseno++)
    {
        int row,cnt=0,ans;

        scanf("%d",&row);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&a[i][j]);
        for(int i=0; i<4; i++)
            tmp[i] = a[row-1][i];

        scanf("%d",&row);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d",&a[i][j]);

        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(a[row-1][i]==tmp[j])
                    cnt++, ans=a[row-1][i];
            }
        }

        printf("Case #%d: ",caseno);
        if(cnt>1)
            printf("Bad magician!\n");
        else if(cnt==1)
            printf("%d\n",ans);
        else
            printf("Volunteer cheated!\n");


    }


    return 0;
}
