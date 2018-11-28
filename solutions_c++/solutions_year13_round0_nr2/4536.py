#include <iostream>
#include <vector>
#include <algorithm>

struct index {
    int id;
    int n;
    int m;

    index(int pid, int pn, int pm)
        : id(pid),
          n(pn),
          m(pm)
    {
    }

    bool operator< (const index& i) const
    {
        return id < i.id;
    }
};

int main()
{
    int a[100][100];
    bool b[100][100];

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, M;
        std::cin >> N >> M;
        std::vector<index> ind;
        ind.reserve(N * M);
        for (int n = 0; n < N; ++n) {
            for (int m = 0; m < M; ++m) {
                b[n][m] = true;
                std::cin >> a[n][m];
                ind.push_back(index(a[n][m], n, m));
            }
        }

        std::sort(ind.begin(), ind.end());

        bool ans = true;

        for (auto i = ind.begin(); i != ind.end(); ++i) {
            if (!b[i->n][i->m]) {
                continue;
            }

            bool ok = true;
            for (int j = 0; j < M; ++j) {
                if (a[i->n][j] > a[i->n][i->m]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                for (int j = 0; j < M; ++j) {
                    if (a[i->n][j] == a[i->n][i->m]) {
                        b[i->n][j] = false;
                    }
                }
                continue;
            }

            ok = true;
            for (int j = 0; j < N; ++j) {
                if (a[j][i->m] > a[i->n][i->m]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                for (int j = 0; j < N; ++j) {
                    if (a[j][i->m] == a[i->n][i->m]) {
                        b[j][i->m] = false;
                    }
                }
                continue;
            }

            ans = false;
            break;
        }

        std::cout << "Case #" << t << (ans ? ": YES\n" : ": NO\n");
    }
}
