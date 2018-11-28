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

int cas;
int Smax;
void doit() {
    scanf("%d", &Smax);

    int ans = 0;

    int psum = 0;
    FOR(i,Smax+1) {
        ans = max(ans, i - psum);

        char ch;
        scanf(" %c", &ch);
        int val = ch - '0';
        assert(0 <= val && val <= 9);

        psum += val;
    }

    printf("Case #%d: %d\n", cas+1, ans);
}

int T;
int main() {
    scanf("%d", &T);
    for (cas = 0; cas < T; ++cas) doit();
}
