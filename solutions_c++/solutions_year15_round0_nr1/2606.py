#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <climits>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
#define MAX_V 1001


int main()
{
    // freopen("in","r",stdin);
    // freopen("output","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int sMax,cur=0,tmp,ans=0;
        scanf("%d",&sMax);
        for(int i=0;i<=sMax;i++){
            scanf("%1d",&tmp);
            if(tmp > 0 && cur < i){
                ans += i - cur;
                cur = i;
            }
            cur += tmp;
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}