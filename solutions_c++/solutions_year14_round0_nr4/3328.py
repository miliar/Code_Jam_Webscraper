#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define SIZE 1005

using namespace std;

int t, n, cas=1;
double a[SIZE], b[SIZE];
bool au[SIZE], bu[SIZE];

int main(void)
{
    //freopen("D-large.in", "r", stdin);
    //freopen("D-large.out", "w", stdout);

    int i, j, k, ans1, ans2;

    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(i=0; i<n; ++i) scanf("%lf", &a[i]);
        for(i=0; i<n; ++i) scanf("%lf", &b[i]);

        sort(a, a+n);
        sort(b, b+n);

        ans1=ans2=0;

        memset(au, false, sizeof(au));
        memset(bu, false, sizeof(bu));
        for(i=0; i<n; ++i)
        {
            for(j=0, k=-1; j<n; ++j)
            {
                if(!au[j])
                {
                    if(k==-1) k=j;
                    if(b[i]<a[j]) { k=j; break; }
                }
            }
            au[k]=true;
            if(b[i]<a[k]) ans1++;
        }

        for(i=0; i<n; ++i)
        {
            for(j=0, k=-1; j<n; ++j)
            {
                if(!bu[j])
                {
                    if(k==-1) k=j;
                    if(a[i]<b[j]) { k=j; break; }
                }
            }
            bu[k]=true;
            if(a[i]>b[k]) ans2++;
        }

        printf("Case #%d: %d %d\n", cas++, ans1, ans2);
    }

    return 0;
}
