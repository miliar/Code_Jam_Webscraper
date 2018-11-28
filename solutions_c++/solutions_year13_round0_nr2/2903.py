#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <bitset>
#include <utility>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define SZ(c) ((int)(c).size())
#define ITER(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FIND(x,c) ((c).find((x))!=(c).end())
#define MP(x,y) make_pair((x),(y))

typedef long long ll;
const int INF=2147483647;
const int MOD=(int)1e9+7;
const int MAX=105;
int a[MAX][MAX],rowm[MAX],colm[MAX];
int main() {
    int T;
    scanf("%d",&T);
    REP(t,T) {
        int n,m;
        scanf("%d%d",&n,&m);
        fill(rowm,rowm+MAX,0);
        fill(colm,colm+MAX,0);
        REP(i,n) {
            REP(j,m) {
                scanf("%d",&a[i][j]);
                rowm[i]=max(rowm[i],a[i][j]);
                colm[j]=max(colm[j],a[i][j]);
            }
        }
        bool flag=true;
        REP(i,n) {
            REP(j,m) {
                if (!(a[i][j]==rowm[i] || a[i][j]==colm[j])) {
                    flag=false;
                    break;
                }
            }
            if (!flag) break;
        }
        printf("Case #%d: ",t+1);
        if (flag) puts("YES");
        else puts("NO");
    }
    return 0;
}
