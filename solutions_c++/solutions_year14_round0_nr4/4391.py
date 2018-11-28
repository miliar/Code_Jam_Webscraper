#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double a[1111], b[1111];

int cas=1;
void work()
{
    int n;
    scanf("%d", &n);

    for(int i=0;i<n;i++) scanf("%lf", a+i);
    for(int i=0;i<n;i++) scanf("%lf", b+i);
    sort(a, a+n);
    sort(b, b+n);

    int ans1=0, ans2=n;

    int t=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]>b[t])
        {
            ans1++;
            t++;
            if(t==n) break;
        }
    }

    t=n-1;
    for(int i=n-1;i>=0;i--)
    {
        if(a[i]<b[t])
        {
            ans2--;
            t--;
            if(t==-1) break;
        }
    }

    printf("Case #%d: %d %d\n", cas++, ans1, ans2);
}

int main()
{
//    freopen("D:/D-large.in", "r", stdin);
//    freopen("D:/out.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    while(T--)
    {
        work();
    }
}
