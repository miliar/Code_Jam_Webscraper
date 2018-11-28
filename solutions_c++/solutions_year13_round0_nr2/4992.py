#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = 1e15;

const int SZ = 105;

int TC, TCC;
void precalc();
void init();

int N, M, D[SZ][SZ];
int Heights[SZ], Count[SZ], HN;
bool Chk[SZ][SZ];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int i, j, k;

    precalc();

    scanf("%d", &TC);
    while(++TCC <= TC) {
        printf("Case #%d: ", TCC);

        init();
        bool ret = true;

        scanf("%d%d", &N, &M);
        for(i = 1; i <= N; i++) {
            for(j = 1; j <= M; j++) {
                scanf("%d", &D[i][j]);
                Heights[++HN] = D[i][j];
                ++Count[D[i][j]];
            }
        }

        sort(Heights + 1, Heights + HN + 1);
        HN = unique(Heights + 1, Heights + HN + 1) - (Heights + 1);
        Heights[++HN] = 100;

        for(k = 1; k < HN && ret; k++) {
            int h = Heights[k], count = 0;
            memset(Chk, 0, sizeof Chk);
            for(i = 1; i <= N; i++) {
                bool canuse = true;
                for(j = 1; j <= M && canuse; j++) if(D[i][j] != h) canuse = false;
                for(j = 1; j <= M && canuse; j++) {
                    if(!Chk[i][j]) ++count;
                    Chk[i][j] = true;
                }
            }

            for(j = 1; j <= M; j++) {
                bool canuse = true;
                for(i = 1; i <= N && canuse; i++) if(D[i][j] != h) canuse = false;
                for(i = 1; i <= N && canuse; i++) {
                    if(!Chk[i][j]) ++count;
                    Chk[i][j] = true;
                }
            }

            if(count != Count[h]) ret = false;
            Count[Heights[k + 1]] += Count[h];
            for(i = 1; i <= N; i++) {
                for(j = 1; j <= M; j++) if(D[i][j] == h) D[i][j] = Heights[k + 1];
            }
        }

        puts(ret ? "YES" : "NO");
    }
    return 0;
}

void init() {
    N = M = HN = 0;
    memset(Heights, 0, sizeof Heights);
    memset(Count, 0, sizeof Count);
    memset(D, 0, sizeof D);
}

void precalc() {
}
