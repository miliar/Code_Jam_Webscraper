#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("magictrick.in.c","r",stdin);
    freopen("magictrick.out","w",stdout);
    int t;
    scanf("%d",&t);
    int t1=0;
    while (t1<t) {
        t1++;
        int i,j;
        int n,m;
        int mat1[5][5],mat2[5][5];
        scanf("%d",&n);
        for (i=0;i<4;i++)
        for (j=0;j<4;j++) scanf("%d",&mat1[i][j]);
        scanf("%d",&m);
        for (i=0;i<4;i++)
        for (j=0;j<4;j++) scanf("%d",&mat2[i][j]);

        int niza[17]={0};
        for (j=0;j<4;j++) {
                niza[mat1[n-1][j]]++;
                niza[mat2[m-1][j]]++;
        }
        int br=0;
        int broj=0;
        for (i=0;i<=16;i++) if (niza[i]>=2) {
                br++;
                broj = i;
        }
        if (br==1) printf("Case #%d: %d\n", t1, broj); else
        if (br>1) printf("Case #%d: Bad magician!\n", t1); else
                  printf("Case #%d: Volunteer cheated!\n", t1);
    }


    return 0;
}
