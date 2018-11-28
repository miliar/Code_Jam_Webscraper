#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;


const int mod = 1e9+7;
const int N = 500200000;
const int M = 5e5+30;
int dig[10];
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,n,cas=1;
    scanf("%d",&t);
    while(t--){
        int cnt = 10;
        scanf("%d",&n);
        printf("Case #%d: ",cas++);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }
        memset(dig,0,sizeof(dig));
        for(int i=n;i<N;i+=n){
            int x = i;
            while(x){
                if(!dig[x%10]){
                    dig[x%10] = true;
                    cnt --;
                }
                x /= 10;
            }
            if(cnt == 0){
                printf("%d\n",i);
                break;
            }
        }
    }
    return 0;
}
