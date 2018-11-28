#include <cassert>
#include <cstdio>
using namespace std;

#define cuErr(err) cuErrFunc((err), #err, __LINE__)
void cuErrFunc(cudaError_t err, const char * expr, int line) {
    if (err == cudaSuccess) return;

    fprintf(stderr, "CUDA error on line %d\n", line);
    fprintf(stderr, "%s\n", expr);
    fprintf(stderr, "%s\n", cudaGetErrorString(err));
    exit(1);
}

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
typedef long long ll;

// 1, i, j, k, -1, -i, -j, -k
int multab[8][8];
const int one = 0, eye = 1, jay = 2, kay = 3;
int negate(int x) { return x ^ 0x4; }
void init() {
    FOR(x,4) multab[one][x] = multab[x][one] = x;
    FR(x,1,4) multab[x][x] = negate(one);

    multab[eye][jay] = kay;
    multab[jay][kay] = eye;
    multab[kay][eye] = jay;

    multab[jay][eye] = negate(kay);
    multab[kay][jay] = negate(eye);
    multab[eye][kay] = negate(jay);

    FOR(x,8) FOR(y,8) {
        int z = multab[x & 0x3][y & 0x3];
        if ((x & 0x4) != (y & 0x4)) z = negate(z);
        multab[x][y] = z;
    }

    assert(multab[negate(kay)][jay] == eye);
}

const int MAX_L = 10000;
const int MAX_REP = 11;
const int MAX_VALS = MAX_L * MAX_REP;

int cas;
int L;
ll X;
int len;
int vals[MAX_VALS];

bool solve() {
    int start = 0;
    int pfx = one;
    while (pfx != eye && start < len) {
        //printf("    vals[%d] = %d\n", start, vals[start]);
        pfx = multab[pfx][ vals[start] ];
        ++start;

        //printf("  [0:%d) -> %d\n", start, pfx);
    }
    if (pfx != eye) return false;

    int end = len;
    int sfx = one;
    while (sfx != kay && end > 0) {
        --end;
        sfx = multab[ vals[end] ][sfx];

        //printf("  [%d:len) -> %d\n", end, sfx);
    }
    if (sfx != kay) return false;

    if (start >= end) return false;

    int mid = one;
    FR(i, start, end) mid = multab[mid][ vals[i] ];
    if (mid != jay) return false;

    return true;
}

void doit() {
    scanf("%d%lld", &L, &X);
    FOR(i,L) {
        char ch;
        scanf(" %c", &ch);
        int val = 1 + (ch - 'i');
        assert(1 <= val && val < 4);
        vals[i] = val;
    }

    if (X > 11) X = X%4 + 8;

    FR(r,1,X) {
        FOR(i,L) {
            int j = r*L + i;
            assert(j < MAX_VALS);
            vals[j] = vals[i];
        }
    }
    len = L*X;

    bool ans = solve();

    printf("Case #%d: %s\n",
        cas+1, ans ? "YES" : "NO");
}

int T;
int main() {
    init();
    scanf("%d", &T);
    for (cas = 0; cas < T; ++cas) doit();
}
