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
const int M = 1000;
const int N = 10;
const double eps = 1e-5;
const double dinf = 1e15;
//const int MOD = 1000000007;
const int inf = INT_MAX;
const int ninf = INT_MIN;
const long long MOD = 1000000007;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int cas = 1;
    scanf("%d",&T);
    while(T --){
        int n;
        char s[M];
        scanf("%d%s",&n,s);
        int ans = 0, cnt = 0;
        for(int i = 1; s[i]; ++ i){
            int val = (s[i - 1] - '0');
            if(cnt + val < i){
                ans += (i - cnt);
                cnt = i;
            }else{
                cnt += val;
            }
        }
        printf("Case #%d: %d\n", cas ++,ans);
    }
    return 0;
}
