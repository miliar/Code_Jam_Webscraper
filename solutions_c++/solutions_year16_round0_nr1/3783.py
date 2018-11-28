#include <stdio.h>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <set>
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
    freopen("A" , "r" ,stdin) ;
    freopen("2" , "w" , stdout) ;
    int ca = 0 ;
    int T ; scanf("%d",&T) ;
    while(T --){
    printf("Case #%d: ",++ca) ;
    int n ;
    cin >> n ;
    if(n == 0) printf("INSOMNIA\n") ;
    else{
        set <int> s ;
        int j = 1 ;
        while(1){
            long long k = (ll)j * n ;
            while(k){
                int x = (k % 10) ;
                s.insert(x) ;
                k /= 10 ;
            }
            if(s.size() == 10) {
                cout << (ll)j*n <<endl ; break ;
            }
            j ++ ;
        }
    }
    }
    return 0 ;
}

