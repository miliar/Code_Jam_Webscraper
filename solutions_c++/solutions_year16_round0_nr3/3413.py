#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(a, n) for (int a = 0; a<(n); ++a)
#define FOR(a, b, c) for (int a = (b); a<=(c); ++a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;
typedef long long LL;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////

#define LEN 16
#define ILE (1<<(LEN-2))

#define CHCE 50

char txt[ILE][40];
LL num[ILE][11];
int dziel[ILE][11];
bool wypisana[ILE];
int mam;

void licz() {
    REP(a, ILE) {
        txt[a][LEN] = 0;
        txt[a][0] = txt[a][LEN-1] = '1';
        REP(b, LEN-2)
            txt[a][b+1] = ((a>>b)&1)+'0';
    }
    FOR(base, 2, 10)
        REP(a, ILE) {
            LL res = 0;
            REP(b, LEN)
                res = res*base+txt[a][b]-'0';
            num[a][base] = res;
        }
    FOR(x, 2, 1<<(LEN-1))
        REP(a, ILE) {
            if (wypisana[a]) 
                continue;
        
            bool ok = 1;

            FOR(base, 2, 10) {
                if (dziel[a][base])
                    continue;
                if (num[a][base]%x)
                    ok = 0;
                else
                    dziel[a][base] = x;
            }
            if (ok) {
                wypisana[a] = 1;
                printf("%s", txt[a]);
                FOR(base, 2, 10)
                    printf(" %d", dziel[a][base]);
                printf("\n");
                if (++mam>=CHCE) 
                    return;
            }
        }
}

int main() {
    printf("Case #1:\n");
    licz();
}
