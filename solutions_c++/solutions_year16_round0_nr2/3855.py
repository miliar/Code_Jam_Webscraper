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
#define mod 10e9+7;
#define inf 0x3f3f3f3f;
#define mem0(x , y)  memset(x , y , sizeof(x))
using namespace std;
char s[1000] ;
int d[1000][2] ;
int main(){
    freopen("3" ,"r" ,stdin) ;
    freopen("2" ,"w" ,stdout) ;
    int T ; scanf("%d",&T) ;
    int ca =0 ;
    while (T --){
        scanf("%s",s) ;
        d[0][0] = 0 ; d[0][1] = 0 ;
        int len = strlen(s) ;
        for(int i=1;i<=len ; i++){
            if(s[i-1] == '+') {
                d[i][1] = d[i-1][1] ;
                d[i][0] = d[i-1][1] + 1 ;
            }
            else if(s[i-1] == '-'){
                d[i][1] = d[i-1][0] + 1 ;
                d[i][0] = d[i-1][0] ;
            }
        }
        printf("Case #%d: %d\n",++ca , d[len][1]) ;
    }
}
