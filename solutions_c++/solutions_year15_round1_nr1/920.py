#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int a[1006];
int n;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        cin>>n;
        scanf("%d",&a[0]);
        int maxn = 0;
        int ans1 = 0;
        int ans2 = 0;
        for(int i=1;i<n;i++)
        {
            scanf("%d",&a[i]);
            int k = a[i-1] - a[i];
            if (k > 0) ans1 += k;
            if (k > maxn) maxn = k;
        }
        for(int i=0;i<n-1;i++)
        {
            if (a[i] > maxn) ans2+=maxn; else ans2+=a[i];
        }
        t++;
        printf("Case #%d: %d %d\n",t,ans1,ans2);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
