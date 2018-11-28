#include <cstdio>
#include <unordered_set>

using namespace std;

unordered_set<int> data;

int main() {
    FILE *fin = fopen("A-large.in.txt", "r");
    FILE *fout = fopen("1_large.txt", "w");
    int T, N, kase = 0;
    fscanf(fin, "%d", &T);
    for (int i = 0; i < T; i++) {
        data.clear();
        fscanf(fin, "%d", &N);
        for (int j = 1; ; j++) {
            int tmp = j * N;
            while (tmp > 0) {
                data.insert({tmp % 10});
                tmp /= 10;
            }
            if (N == 0) break;
            if (data.size() == 10) {
                N = j * N;
                break;
            }
        }
        if (N == 0) {
            fprintf(fout, "Case #%d: INSOMNIA\n", ++kase);
            continue;
        }
        fprintf(fout, "Case #%d: %d\n", ++kase, N);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
