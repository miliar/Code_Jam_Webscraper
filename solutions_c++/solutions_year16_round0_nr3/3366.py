#include<bits/stdc++.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<iostream>
typedef long long LL;
using namespace std;
const int S = 20;//随机算法判定次数，S越大，判错概率越小
LL mult_mod(LL a,LL b,LL mod){ //(a*b)%c a,b,c<2^63
    a %= mod;
    b %= mod;
    LL ans = 0;
    while(b){
        if(b&1){
            ans = ans+a;
            if(ans >= mod)
            ans = ans-mod;
        }
        a <<= 1;
        if(a >= mod) a -= mod;
        b >>= 1;
    }
    return ans;
}
LL pow_mod(LL a, LL b, LL mod){ // a^b%mod
    LL ans = 1;
    a %= mod;
    while(b){
        if(b&1)
            ans = mult_mod(ans, a, mod);
        a = mult_mod(a, a, mod);
        b >>= 1;
    }
    return ans;
}
//以a为基,n-1=x*2^t      a^(n-1)=1(mod n)  验证n是不是合数
//一定是合数返回true,不一定返回false
bool check(LL a, LL n, LL x, LL t){
    LL ret = pow_mod(a, x, n);
    LL last = ret;
    for(int i = 1; i <= t; i++){
        ret = mult_mod(ret, ret, n);
        if(ret == 1&&last !=1 &&last != n-1) return true;//合数
        last = ret;
    }
    return ret != 1;
}
// Miller_Rabin()算法素数判定
//是素数返回true.(可能是伪素数，但概率极小)
//合数返回false;
bool Miller_Rabin(long long n){
    if((n&1) == 0)return false;
    if(n == 2) return true;
    LL x = n-1;
    LL t = 0;
    while((x&1) == 0) { x >>= 1; t++;}
    for(int i = 0; i < S; i++){
        LL a = rand()%(n-1)+1;//rand()需要stdlib.h头文件
        if(check(a, n, x, t))
        return false;//合数
    }
    return true;
}

const int N = 1000000;
bool vis[N+5];
int prime[N], num_prime, f[N];
//素数线性筛+欧拉线性筛
void make(){
    for(int i = 2; i < N; i++){
        if(!vis[i]){
            prime[num_prime++] = i;		//存素数
            f[i] = i;				//i的最小质因数为f[i]
        }
        for(int j=0; j < num_prime&&i*prime[j] < N; j++){
            vis[i*prime[j]] = true;
            f[i*prime[j]] = prime[j];
            if(i%prime[j] == 0)
                    break;
        }
    }
}


int lowbit(int x){ return x&-x;}
int cal(int x){
    int ret = 0;
    for( ; x; x -= lowbit(x), ret++);
    return ret;
}
LL pown[11][32];
int main(){
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);
//    freopen("C-large.in", "r", stdin);
//    freopen("C-large.out", "w", stdout);
    make();

    for(int i = 1; i <= 10; i++){
        pown[i][0] = 1;
        for(int j = 1; j <= 16; j++)
            pown[i][j] = pown[i][j-1]*i;
    }

    int T, ca = 1, j, n;
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", ca++);
        for(int i = ( 1<<(n-1) )+1; j; i += 2){
            if(vis[i] == 0||cal(i)%6) continue ;
            int ret = i;
            LL sum = 0, sum2 = 0;
            for(int tot = 0; ret; tot++, ret >>= 1)
            if(ret&1) sum += pown[6][tot], sum2 += pown[8][tot];
            if(Miller_Rabin(sum)||Miller_Rabin(sum2)) continue ;
            //if(ispri[sum] || ispri[sum2]) continue ;
            j--;
            for(int k = 1 << (n-1); k; k >>= 1)
                printf("%d", (k&i) != 0);
            printf(" %d", f[i]);//2
            printf(" 2");//3
            printf(" 3");//4
            printf(" 2");//5
            printf("");//6
            for(int pp = 0; ; pp++)
                if(sum%prime[pp] == 0){
                    printf(" %d", prime[pp]);
                    break;
                }

            printf(" 2");//7
            printf("");//8
            for(int pp = 0; ; pp++)
                if(sum2%prime[pp] == 0){
                    printf(" %d", prime[pp]);
                    break;
                }
            printf(" 2");//9
            printf(" 3");//10
            printf("\n");
        }


    }
    return 0;
}
