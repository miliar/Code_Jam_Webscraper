#include <cstdio>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 1005;

int n;
char str[maxn];

int main() {
    //freopen("in.cpp", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int T,ncase=0;
    scanf("%d",&T);
    while(T--) {
        scanf("%d%s",&n,str);
        int sum=str[0]-'0',ret=0;
        for(int i=1; i<=n; i++) {
            if(sum<i) {
                int tt=i-sum;
                ret+=tt;
                sum+=tt;
            }
            sum+=str[i]-'0';
        }
        printf("Case #%d: %d\n",++ncase,ret);
    }
    return 0;
}
