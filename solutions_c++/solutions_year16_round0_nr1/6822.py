#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
int T,N,sum;
int flag[15];
void add(LL x){
    while(x){
        if(!flag[x%10]){
            flag[x%10] = 1;
            ++sum;
        }
        x /= 10;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int casei = 1; casei <= T; ++casei){
        scanf("%d",&N);
        if(!N){
            printf("Case #%d: INSOMNIA\n",casei);
            continue;
        }
        sum = 0;
        memset(flag,0,sizeof(flag));
        for(int i = 1; true; ++i){
            LL tmp = (LL) i * N;
            add(tmp);
            if(sum == 10){
                printf("Case #%d: %I64d\n",casei,tmp);
                break;
            }
        }
    }
    return 0;
}
