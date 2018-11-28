#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1e3 + 5;
double a[MAXN],b[MAXN];
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Out.txt","w",stdout);
    int T,n;
    scanf("%d",&T);
    for(int kase = 1;kase <= T;++kase)
    {
        scanf("%d",&n);
        for(int i = 0;i < n;++i)
            scanf("%lf",&a[i]);
        for(int i = 0;i < n;++i)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int cnt1 = 0,cnt2 = 0,rear = n-1;
        for(int i = n-1;i >= 0;--i){
            if(a[rear]>b[i]){
                rear--;
                cnt1++;
            }
        }
        rear = n-1;
        for(int i = n-1;i >= 0;--i){
            if(b[rear] > a[i])
                rear--;
            else
                cnt2++;
        }
        printf("Case #%d: %d %d\n",kase,cnt1,cnt2);
    }
    return 0;
}
