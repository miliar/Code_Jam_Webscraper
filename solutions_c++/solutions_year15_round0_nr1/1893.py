#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;

#define N 1005
#define P 1005
#define INF 1LL<<61
#define LL  long long
#define MOD 1000000007

#define MID ((l + r)/2)
#define lx (x<<1)
#define rx ((x<<1)|1)

char str[N];

int main(){
    //freopen("../in.txt","r",stdin);
    int tt;
    int n;
    scanf("%d",&tt);
    int total;
    int need;
    for(int cas=1;cas<=tt;cas++){
        total = 0;
        need = 0;
        scanf("%d %s",&n,str);
        total = (str[0]-'0');
        for(int i=1;i<n+1;i++){
            int now_num = str[i] - '0';
            if(total < i && now_num>0){
                need += i - total;
                total += i - total;
            }
            total += now_num;
        }
        printf("Case #%d: %d\n",cas,need );
    }
    return 0;
}