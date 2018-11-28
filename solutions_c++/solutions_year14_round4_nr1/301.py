#include<cstdio>
#include<algorithm>
using namespace std;
int a[100010];
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca = 1; ca<=ti; ca++){
        int n,x;scanf("%d%d",&n,&x);
        for(int i = 0; i < n; i ++)
        {
            scanf("%d",a+i);
        }
        sort(a,a+n);
        int l = 0, r = n;
        int cnt = 0;
        while(l < r)
        {
            if(a[l] + a[r-1] <= x)
            {
                l ++;
                r --;
            }
            else  r --;
            cnt ++;
        }
        printf("Case #%d: %d\n",ca,cnt);
    }
}
