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
int main(){
    freopen("1" , "r" , stdin) ;
    freopen("2" , "w" , stdout) ;
    int T , ca = 0 ;
    scanf("%d",&T) ;
    while(T --){
        int n , m ,s ;
        scanf("%d%d%d",&n,&m,&s) ;
        printf("Case #%d: " , ++ca) ;
        for(int i=1;i<s;i++){
            printf("%d " , i) ;
        }
        printf("%d\n" , s) ;
    }
}

