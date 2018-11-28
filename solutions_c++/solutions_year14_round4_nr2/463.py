#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

const int MAXN = 1000;

int N;
int A[MAXN];
map<int, bool> mark;

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) scanf("%d", &A[i]);
        mark.clear();
        int answer = 0;

        while (true) {
            int mxi = -1;
            for (int i = 0; i < N; ++i)
                if (!mark[A[i]] && (mxi == -1 || A[mxi] > A[i])) mxi = i;

            if (mxi == -1) break;

            mark[A[mxi]] = true;

            int ku = mxi, kd = mxi;

            while (ku+1<N && A[ku+1]>A[mxi]) ++ku;
            while (kd-1>=0 && A[kd-1]>A[mxi]) --kd;

            if (ku-mxi < mxi-kd)
                while (mxi+1<N && A[mxi] < A[mxi+1]) { swap(A[mxi], A[mxi+1]); ++answer; ++mxi; }
            else
                while (mxi-1>=0 && A[mxi] < A[mxi-1]) { swap(A[mxi], A[mxi-1]); ++answer; --mxi; }
        }

        printf("%d\n", answer);
    }

    return 0;
}
