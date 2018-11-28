#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#define rep(i,j,n) for(int i=j;i<n;i++)
#define repd(i,j,n) for(int i=j;i>n;i--)
#define N 1005
using namespace std;
double a[N],b[N];
bool flag[N];
int n;
int main()
{

 //freopen("in.txt","r",stdin);
 //freopen("out.txt","w",stdout);
    int T;
    scanf("%d", &T);
    int test=1;
    while(T--)
    {
        scanf("%d", &n);
        int p1 = 0, p2 = 0;
        memset(flag, true, sizeof(flag));
        for (int i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
        }
         for (int i=0;i<n;i++)
        {
            scanf("%lf", &b[i]);
        }
        sort(a, a+n);
        sort(b, b+n);
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<n;j++)
            {
                if (a[j]>b[i]&&flag[j])
                {
                    p1++;
                    flag[j]=false;
                    break;
                }
            }
        }
        memset(flag, true, sizeof(flag));
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<n;j ++)
            {
                if (b[j]>a[i]&&flag[j])
                {
                    p2++;
                    flag[j]=false;
                    break;
                }
            }
        }

        printf("Case #%d: %d %d\n",test++, p1, n-p2);
    }
    return 0;
}
