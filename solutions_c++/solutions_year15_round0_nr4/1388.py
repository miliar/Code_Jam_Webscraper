/*************************************************************************
    > File Name: gcja.cpp
    > Author: Lawrence_
    > Mail: 402374437@qq.com
    > Created Time: 2015/4/11 21:29:59
 ************************************************************************/
#include <cstdio>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <deque>
#include <list>
#include <map>
#include <vector>
#include <cstdlib>
#include <set>
#include <cctype>
#define ll long long
#define lson l,m,rt << 1
#define rson m+1,r,rt << 1 | 1
#define pi acos(-1)
#define INF 0x7f7f7f7f
#define Clear(name,init) memset(name,init,sizeof(name))
#define eps 1e-8
using namespace std;
int main(){
   // freopen("C:\\Users\\joho\\Desktop\\D-small-attempt0.in","r+",stdin);
   // freopen("C:\\Users\\joho\\Desktop\\A-small-attempt1.out","w+",stdout);
    int t;
    while(~scanf("%d",&t)){
        for(int cas = 1;cas <= t; cas++){
            int x,r,c;
            scanf("%d%d%d",&x,&r,&c);
            if(x == 1){
                printf("Case #%d: GABRIEL\n",cas);
                continue;
            }
            else if(x == 2){
                if(r % 2 == 0 || c % 2 == 0){
                    printf("Case #%d: GABRIEL\n",cas);
                    continue;
                }
                else{
                     printf("Case #%d: RICHARD\n",cas);
                    continue;
                }
            }
            else if(x == 3){
                if((r == 2 && c == 3) || (r == 3 && c == 2) || (r == 4 && c == 3) || (r == 3 && c == 4) || (r == 3 && c == 3)){
                    printf("Case #%d: GABRIEL\n",cas);
                    continue;
                }
                else{
                    printf("Case #%d: RICHARD\n",cas);
                    continue;
                }
            }
            else if(x == 4){
                if((r == 4 && c == 3) || (r == 3 && c == 4) || (r == 4 && c == 4)){
                    printf("Case #%d: GABRIEL\n",cas);
                    continue;
                }
                else{
                    printf("Case #%d: RICHARD\n",cas);
                    continue;
                }
            }
        }
    }
    return 0;
}
