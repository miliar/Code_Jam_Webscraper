#include <bits/stdc++.h>
using namespace std;
int hav[1010];
int solve(int x,int n)
{
    int now = hav[0] + x,f = 1;
        for(int i = 1;i <= n;i ++){
            if(now >= i)
                now += hav[i];
            else
                f = 0;
        }
    return f;
}
int main()
{
    int T,ca = 0,n;
    scanf("%d",&T);
    freopen("out.txt","w",stdout);
    while(T--){
        scanf("%d",&n);
        for(int i = 0;i <= n;i ++) scanf("%1d",&hav[i]);
        for(int i = 0;i <= n;i ++)
        if(solve(i,n)){
            printf("Case #%d: %d\n",++ca,i);
            break;
        }
    }
    return 0;
}
