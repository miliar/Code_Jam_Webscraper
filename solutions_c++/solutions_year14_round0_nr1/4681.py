#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>
#include<vector>
#include<queue>
#include<string.h>
#include<algorithm>
using namespace std;
#define N 1000000
#define mod 1000000007
#define ll long long
#define ex 2.7182818284590452354
#define pi 3.141592653589793239
#define INFF 999999999
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int a[5][5],b[5][5];
int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    while(scanf("%d",&t)!=EOF)
    {
        for(int Case=1;Case<=t;Case++)
        {
            int add=0,zx;
            int x,y,i,j;
            scanf("%d",&x);
            for(i=1;i<=4;i++)
            {
                for(j=1;j<=4;j++)
                    scanf("%d",&a[i][j]);
            }
            scanf("%d",&y);
            for(i=1;i<=4;i++)
            {
                for(j=1;j<=4;j++)
                    scanf("%d",&b[i][j]);
            }
            printf("Case #%d: ",Case);
            for(i=1;i<=4;i++)
            {
                for(j=1;j<=4;j++)
                {
                    if(a[x][i]==b[y][j])
                    {
                        add++;
                        zx=a[x][i];
                        break;
                    }
                }
            }
            if(add==1)
                printf("%d\n",zx);
            else
            {
                if(add==0)
                    printf("Volunteer cheated!\n");
                else
                    printf("Bad magician!\n");
            }
        }
    }
    return 0;
}
