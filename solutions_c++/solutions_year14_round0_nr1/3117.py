#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int map1[5][5];
int map2[5][5];
int main()
{
    int ca;
    int a[5],b[5];
    freopen("F:\\1.in","r", stdin);
	freopen("F:\\1me.txt", "w", stdout);
	
    scanf("%d",&ca);
	int n,m,i,j, x;
    int cc=0;
    while(ca--)
    {
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&map1[i][j])  ;
            }
        }
        scanf("%d",&m);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&map2[i][j])  ;

            }
        }

        int cnt=0;
        int ans=-1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            if(map1[n][i]==map2[m][j])
            {
                cnt++;
                ans=map1[n][i];
            }
        printf("Case #%d: ",++cc);
        if(cnt==0)printf("Volunteer cheated!\n");
        else
        {
            if(cnt>1)printf("Bad magician!\n");
            else printf("%d\n",ans);
        }
    }
    return 0;
}






