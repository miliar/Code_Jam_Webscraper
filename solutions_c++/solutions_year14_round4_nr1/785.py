#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t, n, a, nn[705], x, ma, i, j;
    scanf("%d",&t);
    for(int cnt =1; cnt<= t;cnt++){
        scanf("%d%d",&n,&x);
        memset(nn,0,sizeof(nn));
        ma = 0;
        for(i=0;i<n;i++){
            scanf("%d",&a);
            nn[a] ++;
            ma = max(ma, a);
        }
        int ret = 0, rest = n;
        while(rest){
            int p = ma;
            nn[p] --;
            rest --;
            for(j=x-p;j>=0;j--){
                if(nn[j]){
                    nn[j] --;
                    rest--;
                    break;
                }
            }
            ret ++;
            if((nn[p] == 0)&&rest){
                while(nn[ma] == 0)
                    ma--;
            }
        }
        printf("Case #%d: %d\n",cnt,ret);
    }
    return 0;
}
