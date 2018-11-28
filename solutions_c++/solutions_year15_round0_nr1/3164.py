#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define MP make_pair

typedef long double DB;
typedef long long LL;
typedef pair <int, int> PI;

const DB eps = 1e-8;
const int N = 2e5 + 7;
const int INF = 1e9 + 7;
const int MOD = 1e9 + 7;


int CAS, n;
char s[N];


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d", &n);
        scanf("%s", s);
        int sum = 0, ans = 0;
        for (int i = 0; i <= n; i++){
            if (sum >= i) sum += s[i] - '0';
            else{
                if (s[i] != '0'){
                    ans += i - sum;
                    sum = i + s[i] - '0';
                }
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
