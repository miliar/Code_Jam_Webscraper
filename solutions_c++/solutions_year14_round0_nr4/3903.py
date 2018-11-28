#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    FILE *in = fopen("D-large.in", "r");
    FILE *out = fopen("D-large.out", "w");

    int T;
    fscanf(in, "%d", &T);

    int testCase;
    for (testCase = 1; testCase <= T; testCase++) {
        int N;
        fscanf(in, "%d", &N);

        vector <double> naomis;
        vector <double> kens;

        int k;
        for (k = 0; k < N; k++) {
            double s;
            fscanf(in, "%lf", &s);

            naomis.push_back(s);
        }

        for (k = 0; k < N; k++) {
            double s;
            fscanf(in, "%lf", &s);

            kens.push_back(s);
        }

        sort(naomis.begin(), naomis.end());
        sort(kens.begin(), kens.end());

        vector <double> n2 = naomis;
        vector <double> k2 = kens;

        int war = 0, dwar = 0;
        int turn;
        for (turn = 0; turn < N; turn++) {
            double n = n2[0];

            if (n > k2[k2.size() - 1]) {
                ++war;

                n2.erase(n2.begin());
                k2.erase(k2.begin());
            } else {
                int i = 0;
                while (k2[i] < n) {
                    ++i;
                }

                k2.erase(k2.begin() + i);
                n2.erase(n2.begin());
            }
        }

        while (naomis.size() > 0) {
            if (naomis[0] > kens[0]) {
                ++dwar;
                naomis.erase(naomis.begin());
                kens.erase(kens.begin());
            } else {
                naomis.erase(naomis.begin());
            }
        }

        fprintf(out, "Case #%d: %d %d\n", testCase, dwar, war);
    }

    fclose(in);
    fclose(out);
}