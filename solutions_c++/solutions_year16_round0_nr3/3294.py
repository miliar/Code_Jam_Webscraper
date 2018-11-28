#include <stdio.h>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#define inf 0x3f3f3f3f
#define mem0(x , y)  memset(x , y , sizeof(x))
#define ll long long
#define REP(x , y)   for(int i=0;i<y;i++)
#define FOR(x , y)   for(int i=1;i<y;i++)
#define lowbit(x) (x & (-x))
#define read(x) scanf("%d",&x)
using namespace std ;
int dig[160] , td = 0 ;
int dv[140] ;
bool judge(ll num , int base){
    for(int i=2;i<=sqrt(num);i++){
        if(num % i == 0){
            dv[base] = i ;
            return true ;
        }
    }
    return false ;
}
int main(){
    freopen("1" , "r" ,stdin) ;
    freopen("2" , "w" , stdout) ;
    int T ; scanf("%d",&T) ;
    int cnt = 0 ;
    int n , m ;
    scanf("%d%d",&n,&m) ;
    printf("Case #1:\n") ;
    int tmp = (1 << (n-1));
    for(int i=0; i < (1<<(n-2)) ;i++){
        int k = tmp + i*2 + 1 ;
        int td = 0 ;
        while(k){
            dig[td++] = k % 2 ;
            k /= 2 ;
        }
        int f = 1 ;
        for(int j=2;j<=10;j++){
            ll num = 0 ;
            for(int z=td-1;z>=0;z--){
                num *= j ;
                num += dig[z] ;
            }
            if(judge(num , j) != 1) f = 0 ;
        }
        if(f == 1) {
            for(int j=td-1;j>=0;j--) printf("%d",dig[j]) ;
            printf(" ") ;
            for(int j=2;j<10;j++) printf("%d ",dv[j]) ; printf("%d\n",dv[10]) ;
            cnt ++ ;
        }
        if(cnt == m) break ;
    }
}

