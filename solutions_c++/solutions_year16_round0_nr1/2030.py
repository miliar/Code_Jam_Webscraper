#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#define PB push_back
#define MP make_pair
#define LB lower_bound
#define UB upper_bound
#define FT first
#define SD second
#define VI vector<int>
#define MII map<int,int>
#define SI set<int>
#define rep(i, n) for (int i = 0; i < n; i++)
typedef long long LL;
typedef long double LD;
//const int INF = 0x7FFFFFFF;
//const LL LINF = 0x7FFFFFFFFFFFFFFFll;

using namespace std;

int main(){
    
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int b[10];
    int casenum, ans;
    int n;
    scanf("%d", &casenum);
    for (int z = 1; z <= casenum; z++){
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", z);
        }
        else {
            ans = 0;
            int cnt = 0;
            memset(b, 0, sizeof b);
            while (cnt < 10) {
                ans += n;
                int tmp = ans;
                while (tmp > 0){
                    if (b[tmp % 10] == 0){
                        cnt++;
                        b[tmp % 10] = 1;
                    }
                    tmp /= 10;
                }
            }
            printf("Case #%d: %d\n", z, ans);
        }
        
    }
    
    fclose(stdin);
    fclose(stdout);
    
}