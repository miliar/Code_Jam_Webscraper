#include <stdio.h>
#include <cstring>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <stack>
#include <cstdlib>
#include <algorithm>
using namespace std;
typedef long long LL;
#define eps 1e-9
#define mod 1000000007
int s[11];
void flag(LL a){
    while(a != 0){
        if(s[a%10] == 0){
            s[a%10] = 1;
        }
        a/=10;
    }
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int i = 1 ;i <= n; i++){
        LL a;
        memset(s,0,sizeof(s));
        scanf("%lld",&a);
        int p = 0;
        int tm = 0;
        LL cm = 0;
        int mark = a;
        if(a != 0){
            while(1){
                p = 0;
                flag(cm);
                for(int j = 0 ;j < 10 ;j++){
                    if(s[j] == 1){
                        p++;
                    }
                }
                if(p == 10){
                    tm = cm;
                    break;
                }
                cm += mark;
            }
        }
        if(a == 0){
            printf("Case #%d: INSOMNIA\n",i);
        }
        else{
            printf("Case #%d: %d\n",i,tm);
        }
    }
}
