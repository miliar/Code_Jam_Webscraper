#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <assert.h>
#include <ctype.h>
//#include <tr1/unordered_set>
//#include <tr1/unordered_map>
#include <bitset>
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
#define inf 1e9
#define debug(a) cout << #a" = " << (a) << endl;
#define debugarry(a, n) for (int i = 0; i < (n); i++) { cout << #a"[" << i << "] = " << (a)[i] << endl; }
#define clr(x, y) memset(x, y, sizeof x)
#define LL long long
#define ll long long
#define uLL unsigned LL
#define ull long long

using namespace std;

int n,j;
void print(ll x){
    for(int i=n-1;i>=0;i--)
        printf("%d",(x>>i)&1);
}

bool cal(ll x,int k,int c){
    int r = 0;
    for(int i=n-1;i>=0;i--){
        r = (r * k )%c;
        if( x & (1<<i) )
            r = (r+1)%c;
    }
    return r == 0;
}

bool cal(ll x){
    for(int i=2;i<=10;i++){
        int is = 0;
        for(int j=2;j<=19;j++){
            if( cal(x,i,j) ){
                is = 1;
                break;
            }
        }
        if( !is ) return false;
    }
    print(x);
    for(int i=2;i<=10;i++){
        for(int j=2;j<=19;j++){
            if( cal(x,i,j) ){
                printf(" %d",j);
                break;
            }
        }
    }
    puts("");
    return true;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    while(T--){
        printf("Case #1:\n");
        scanf("%d%d",&n,&j);
        ll x = (1 | (1<<n-1));
        for(ll i=0;j;i+=2){
            if( cal( x|i ) )
                j--;
            //debug(i);
        }
    }
    return 0;
}












