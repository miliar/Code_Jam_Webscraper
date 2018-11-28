#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<algorithm>
#include<map>
#include<climits>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<bitset>
#include<set>
#include<cmath>
#include<list>
#include<sstream>
using namespace std;
const int M = 1010;
const int N = 10;
const double eps = 1e-5;
const double dinf = 1e15;
//const int MOD = 1000000007;
const int inf = INT_MAX;
const int ninf = INT_MIN;
const long long MOD = 1000000007;
int arr[M];


int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int cas = 1;
 //   inits();
    scanf("%d",&T);
    while(T --){
        int n;
        scanf("%d",&n);
        int ans = INT_MAX, maxval = INT_MIN;
        for(int i = 0; i < n; ++ i){
            scanf("%d",&arr[i]);
            maxval = max(arr[i], maxval);
        }
        for(int i = 1; i <= maxval; ++ i){
            int cnt = 0;
            for(int j = 0; j < n; ++ j){
                if(arr[j] > i){
                    cnt += arr[j]/i;
                    if(arr[j]%i == 0)
                        -- cnt;
                }
            }
            ans = min(ans, i + cnt);
        }
        printf("Case #%d: %d\n", cas ++,ans);
    }
    return 0;
}
