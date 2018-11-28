/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
#define INF 0x7fffffff
const double eqs=1e-8;
int a[10][10];
int b[10][10];
int main()
{
    int t,cnt=0;
    //freopen("A-small-attempt3.in" , "r" , stdin);
    //freopen("A-small-attempt3.out" , "w" , stdout);
    scanf("%d",&t);
    while(t--)
    {
        int x1,x2;
        scanf("%d",&x1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&x2);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        int sum=0,temp;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a[x1][i]==b[x2][j])
                {
                    sum++;
                    temp=a[x1][i];
                }
            }
        }
        printf("Case #%d: ",++cnt);
        if(sum==1)
            printf("%d\n",temp);
        else if(sum==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
