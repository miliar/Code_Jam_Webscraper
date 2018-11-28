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

const bool USE_GPU = true;

const int MAXD = 1024;
const int MAXP = 1024;

__global__ void tryOneMax(int * d_yofm, int * d_Pi, int D) {
    int m = 1 + blockIdx.x * blockDim.x + threadIdx.x;

    int ans = m;
    FOR(i,D) {
        ans += (d_Pi[i] - 1) / m;
    }

    d_yofm[m] = ans;
}

int cas;
int D;
int h_Pi[MAXD];
int h_yofm[MAXP];
void doit() {
    scanf("%d", &D);
    FOR(i,D) {
        scanf("%d", &h_Pi[i]);
    }

    int ans = MAXP;
    if (USE_GPU) {
        const int Pi_BYTES = sizeof(int) * D;
        int * d_Pi;
        cuErr(cudaMalloc(&d_Pi, Pi_BYTES));
        cuErr(cudaMemcpy(d_Pi, h_Pi, Pi_BYTES, cudaMemcpyHostToDevice));

        const int yofm_BYTES = sizeof(int) * MAXP;
        int * d_yofm;
        cuErr(cudaMalloc(&d_yofm, yofm_BYTES));

        tryOneMax<<<1, MAXP-1>>>(d_yofm, d_Pi, D);
        cudaDeviceSynchronize();
        cuErr(cudaGetLastError());

        cuErr(cudaMemcpy(h_yofm, d_yofm, yofm_BYTES, cudaMemcpyDeviceToHost));
        FR(i,1,MAXP) ans = min(ans, h_yofm[i]);
    } else {
        FR(m,1,MAXP) {
            int ret = m;
            FOR(i,D) ret += (h_Pi[i] - 1) / m;
            ans = min(ans, ret);
        }
    }

    printf("Case #%d: %d\n", cas+1, ans);
}

int T;
int main() {
    scanf("%d", &T);
    for (cas = 0; cas < T; ++cas) doit();
}
