#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

bool lawnable(int a[100][100], int R, int C)
{
    int horizen[100];
    int vertical[100];
    for (int i=0; i<R; ++i) {
        horizen[i] = 0;
    }
    for (int i=0; i<C; ++i) {
        vertical[i] = 0;
    }
    for (int r=0; r<R; ++r) {
        for(int c=0; c<C; ++c) {
            horizen[r] = max(horizen[r], a[r][c]);
            vertical[c] = max(vertical[c], a[r][c]);
        }
    }
    for (int r=0; r<R; ++r) {
        for (int c=0; c<C; ++c) {
            if (a[r][c] != min(horizen[r], vertical[c])) {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char** argv)
{
    FILE *input, *output;
    if (argc==2) {
        input = fopen(argv[1], "r");
        output = fopen((string(argv[1])+".out").c_str(), "w");
    } else {
        return 1;
    }
    int T;
    fscanf(input, "%d", &T);
    for (int z=1; z<=T; ++z) {
        int N, M;
        int a[100][100];
        fscanf(input, "%d %d", &N, &M);
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                fscanf(input, "%d", &a[i][j]);
            }
        }
        fprintf(output, "Case #%d: ", z);
        if (lawnable(a, N, M)) {
            fputs("YES\n", output);
        } else {
            fputs("NO\n", output);
        }
    }
    return 0;
}
