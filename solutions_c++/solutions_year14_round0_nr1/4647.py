#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;
int a[5][5],b[5][5];
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int i,j,k,m,n;
    int ca;
    int t=1;
    scanf("%d",&ca);
    while(scanf("%d",&n)!=EOF)
    {
int tt=0;

        tt++;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++){
            scanf("%d",&a[i][j]);
            tt++;
    }
        scanf("%d",&m);
tt++;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++){
            scanf("%d",&b[i][j]);
tt++;
    }
        vector<int> v;
        v.clear();
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                if(a[n][i]==b[m][j])
                {
                    v.push_back(a[n][i]);
                    break;
                }
        printf("Case #%d: ",t++);

        if(v.size()==0)
            printf("Volunteer cheated!\n");
        else if(v.size()>=2)
            printf("Bad magician!\n");
        else
            printf("%d\n",v[0]);


    }



    return 0;
}
