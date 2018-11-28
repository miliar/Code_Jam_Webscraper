#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        int N;
        int X;
        scanf("%d%d", &N, &X);
        int *filesize = new int[N];
        bool *done = new bool[N];
        for (int j = 0; j < N; ++j)
        {
            scanf("%d", &filesize[j]);
            done[j] = false;
        }
        sort(filesize, filesize+N);
        int ans = 0;
        for (int j = N-1; j >= 0; --j) {
            if (done[j])
                continue;
            ++ans;
            for (int k = j-1; k >= 0; --k) {
                if (done[k]) continue;
                if (filesize[k] + filesize[j] > X) continue;
                done[k] = true;
                break;
            }
        }
        printf("%d\n", ans);
        delete [] filesize;
        delete [] done;
    }
    return 0;
}
