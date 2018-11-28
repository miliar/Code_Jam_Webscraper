#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    int cases=0;
    freopen("nn.in","r",stdin);
    freopen("output.in","w",stdout);
    scanf("%d",&T);
    while(T--){
        cases++;
        int n;
        printf("Case #%d: ",cases);
        scanf("%d",&n);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        int d=0;
        int mask=1023;
        while(mask){
            d+=n;
            int it=d;
            while(it){
                int cur=it%10;
                it/=10;
                if(mask&(1<<cur)){
                    mask^=(1<<cur);
                }
            }
        }
        printf("%d\n",d);
    }
    return 0;
}
