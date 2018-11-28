#include <iostream>
#include <queue>
#include <map>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
#define maxn 1005
char s[maxn];

int main(){
    int T,smax,cas = 1;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&smax);
        scanf("%s",s);
        int res = 0;
        int cur = 0;
        for(int i=0;i<=smax;++i){
            int curLev = s[i] - '0';
            if(curLev == 0) continue;
            if(cur < i){
                int tmp = i-cur;
                res += tmp;
                cur = cur+curLev+tmp;
            }
            else
                cur += curLev;
        }
        printf("Case #%d: %d\n",cas++,res);
    }
    return 0;
}
