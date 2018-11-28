//author: CHC
//First Edit Time:	2015-04-11 09:56
//Last Edit Time:	2015-04-11 09:56
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <limits>
using namespace std;
typedef long long LL;
const int MAXN=1e+4;
const int MAXM=1e+5;
const int INF = numeric_limits<int>::max();
const LL LL_INF= numeric_limits<LL>::max();
char strs[MAXN];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cas=0,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d %s",&n,strs);
        int cnt=strs[0]-'0',cnt1=0;
        for(int i=1;strs[i];i++){
            //printf("%d %d %d\n",i,cnt,cnt1);
            if(i>cnt){
                cnt1+=i-cnt;
                cnt+=i-cnt;
            }
            cnt+=strs[i]-'0';
            //printf("%d %d %d\n",i,cnt,cnt1);
        }
        printf("Case #%d: %d\n",++cas,cnt1);
    }
    return 0;
}
