#include <iostream>

using namespace std;

int main()
{
    int tt,rr=1;
    scanf("%d",&tt);
    while(tt--)
    {
        int m,n;
        int grass[100][100];
        scanf("%d %d",&m,&n);
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
            {
                scanf("%d",&grass[i][j]);
            }
        int hori[100],vert[100];
        for (int i=0;i<100;i++)
            hori[i]=vert[i]=0;
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
            {
                if (hori[i]<grass[i][j]) hori[i]=grass[i][j];
                if (vert[j]<grass[i][j]) vert[j]=grass[i][j];
            }
        int flag=1;
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
                if (grass[i][j]<hori[i] && grass[i][j]<vert[j]) flag=0;
        printf("Case #%d: ",rr++);
        if (flag) printf("YES\n");
        else printf("NO\n");

    }
    return 0;
}
