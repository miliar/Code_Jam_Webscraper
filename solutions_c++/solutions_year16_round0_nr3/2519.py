#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#define LL long long
#define maxn 100100
#define inf 0x3f3f3f3f
#define IN freopen("in.txt","r",stdin);
using namespace std;

LL divs[15];
int check(LL x){
    for(LL i=2; i*i<=x; i++){
        if(x%i == 0) return i;
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    IN;
    freopen("out.txt","w",stdout);

    int t,ca=1; cin >> t;
    while(t--)
    {
        printf("Case #%d:\n",ca++);
        int l;
        int k;
        cin >> l >> k;
        int cnt = 0;

        for(LL i=(1<<(l-1))+1; i<(1<<l); i+=2){
            int b;
            for(b=2; b<=10; b++){
                LL j = i;
                LL tmp = 1;
                LL ans = 0;
                while(j){
                    if(j%2 == 1) ans += tmp;
                    tmp *= b;
                    j /= 2;
                }

                LL x = check(ans);
                if(!x) break;
                divs[b] = x;
            }
            if(b == 11){
                char ss[50] = {0};
                LL ttt = i;
                for(int j=l-1; j>=0; j--){
                    if(ttt%2) ss[j] = '1';
                    else ss[j] = '0';
                    ttt /= 2;
                }
                printf("%s ", ss);
                printf("%lld",divs[2]);
                for(int z=3; z<=10; z++)
                    printf(" %lld", divs[z]);
                printf("\n");

                cnt++;
                if(cnt == k) break;
            }
        }
    }

    return 0;
}
