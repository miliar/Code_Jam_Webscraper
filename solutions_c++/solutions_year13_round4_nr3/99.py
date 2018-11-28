#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double du;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)
const int MAXN = 2004;

int d[MAXN];
bool a[MAXN][MAXN];
int s[MAXN];
int pre[MAXN];
int x[MAXN];

void insert(int i, int j){
    if(a[i][j] == 0){
        a[i][j] = 1;
        d[j]++;
    }
}

int main()
{
    #ifdef __FIO
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int T, i0;
    scanf("%d", &T);
    for(i0 = 1; i0 <= T; i0++){
        printf("Case #%d: ", i0);
        int n;
        int i, j, k;
        scanf("%d", &n);
        memset(a, 0, sizeof a);
        memset(d, 0, sizeof d);
        for(i = 1; i <= n; i++)
            scanf("%d", &s[i]);
        memset(pre, -1, sizeof pre);
        for(i = 1; i <= n; i++){
            if(pre[s[i]] != -1)
                insert(i, pre[s[i]]);
            if(pre[s[i]-1] != -1)
                insert(pre[s[i]-1], i);
            pre[s[i]] = i;
        }
        for(i = 1; i <= n; i++)
            scanf("%d", &s[i]);
        memset(pre, -1, sizeof pre);
        for(i = n; i >= 1; i--){
            if(pre[s[i]] != -1)
                insert(i, pre[s[i]]);
            if(pre[s[i]-1] != -1)
                insert(pre[s[i]-1], i);
            pre[s[i]] = i;
        }
        for(i = 0; i < n; i++){
            j = 1;
            while(d[j])
                j++;
            x[j] = i+1;
            for(k = 1; k <= n; k++)
                if(a[j][k])
                    d[k]--;
            d[j] = 1<<20;
        }
        printf("%d", x[1]);
        for(i = 2; i <= n; i++)
            printf(" %d", x[i]);
        printf("\n");
    }
    return 0;
}
