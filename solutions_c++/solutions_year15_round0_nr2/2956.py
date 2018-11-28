#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int n;
int a[1024];
int c[1024];
#define M (1000)

int main()
{
    int T;
    int ca = 1;
    scanf("%d",&T);
    while(T--)
    {
        int ans = M;
        memset(c,0,sizeof(c));
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(int i=1;i<=M;i++)
        {
            int tmp = i;
            for(int j=0;j<n;j++)
            {
                tmp += (a[j]+i-1)/i - 1;
            }
            if( ans > tmp ) 
                ans = tmp;
            if( ans < i ) break;
        }
        printf("Case #%d: %d\n",(ca++),ans);
    }
    return 0;
}

