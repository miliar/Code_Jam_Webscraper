#include<stdio.h>
#include<algorithm>
#include<cmath>
using namespace std;
int a[5][5],b[5][5];
int main()
{
    int n,t;
     freopen("hehe.in","r",stdin);
     freopen("hello.out","w",stdout);
     scanf("%d",&t);
    for (int k=1;k<=t;k++)
    {
        printf("Case #%d: ",k);
        scanf("%d",&n);
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
            scanf("%d",&a[i][j]);
           int m;
        scanf("%d",&m);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
            scanf("%d",&b[i][j]);
            int ans=0,lp;
          for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++)
        if (a[n][i]==b[m][j]) {lp=a[n][i];ans++;}
          if (ans==0) printf("Volunteer cheated!\n");
            else if (ans==1) printf("%d\n",lp);
            else printf("Bad magician!\n");
    }
    return 0;
}
