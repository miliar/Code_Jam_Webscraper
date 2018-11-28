#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

vector<double> Nao;
vector<double> Ken;


int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);

    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        Nao.clear();
        Ken.clear();
        int N;
        double t;
        cin >> N;
        for (int i = 0; i < N; ++i) {
            cin >> t;
            Nao.push_back(t);
        }
        for (int i = 0; i < N; ++i) {
            cin >> t;
            Ken.push_back(t);
        }

        sort(Nao.begin(), Nao.end());
        sort(Ken.begin(), Ken.end());

//        for (int j = 0; j < N; ++j)
//            cout << Nao[j] << " ";
//        cout << endl;
//
//        for (int j = 0; j < N; ++j)
//            cout << Ken[j] << " ";
//        cout << endl;

        int i = 0, j = 0, x = N - 1, y = N - 1, d_score = 0;
        bool last = true;

        while (last) {
            if (x == i)
                last = false;
            if (Nao[x] > Ken[y]) {
                x--;
                y--;
                d_score++;
            }
            else if (Nao[i] > Ken[j]) {
                i++;
                j++;
                d_score++;
            }
            else {
                i++;
                y--;
            }
        }

        int score = 0;
        for (int u = 0, v = 0; u < N && v < N; ) {
            if (Nao[u] < Ken[v]) {
                u++;
                v++;
            }
            else {
                v++;
                score++;
            }
        }

        cout << "Case #" << c << ": " << d_score << " " << score << endl;

    }

    return 0;
}

