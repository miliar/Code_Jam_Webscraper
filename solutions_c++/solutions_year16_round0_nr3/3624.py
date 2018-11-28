#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <cmath>
#include <queue>
#include <set>
#include <functional>
using namespace std;

typedef long long LL;

int T;
int n,j;
LL ans[11];

LL pow_bin(LL x,LL e){
    LL res = 1;
    while( e ) {
        if( e&1 ) res = res * x;
        x *= x;
        e>>=1;
    }
    return res;
}


LL f(LL x){
    for(LL i = 2LL; i*i < x ; i++ ) {
        if( x % i == 0 ) return i;
    }
    return -1;
}

LL convert(int x,int base){
    int cnt = 0;
    LL res = 0;
    while( x ) {
        if( x & 1 ){
            res += pow_bin(base,cnt);
        }
        cnt++;
        x >>= 1;
    }
    return res;
}

void print(int x) {
    vector<int> v;
    while( x ) {
        if( x&1 ) {
            v.push_back(1);
        } else {
            v.push_back(0);
        }
        x>>=1;
    }
    for(int i = v.size()-1; i>=0 ; i-- ) {
        printf("%d",v[i]);
    }
}

int main() {
    int cases = 0;
    scanf("%d",&T);
    while( T-- ) {
        printf("Case #%d:\n",++cases);
        scanf("%d%d",&n,&j);
        int cnt = 0;
        for(int i = 1<<(n-1) ; i < (1<<(n)) - 1 ; i++ ) {
            //printf("******%d\n",i);
            if(!(i&1)) continue;
            int ptr = 0;
            LL factor = f(i);
            //printf("factor = %lld\n",factor);
            
            if( factor == -1 ) continue;
            else ans[ ptr++ ] = factor;
            
            bool flag = true;
            
            for(int j = 3; j <= 10 ; j++ ) {
                LL num = convert(i,j);
                //printf("num = %lld\n",num);
                factor = f(num);
                //printf("factor = %lld\n",factor);
                if( factor == -1 ) {
                    flag = false;
                    break;
                } else {
                    ans[ptr++] = factor;
                }
            }
            if( !flag ) continue;
            print(i);
            for(int i = 0 ; i < ptr; i++  ) {
                printf(" %lld",ans[i]);
            }
            printf("\n");
            cnt++;
            if( cnt == j ) break;
        }
    }
    return 0;
}