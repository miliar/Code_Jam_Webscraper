#include <iostream>
#include <cstdio>

using namespace std;
int N, M;
int a[110][110];
int nr_case = 1;

bool isLegal(int x, int y) {
    int count = 0;
    for (int i = 0; i < N; i++)
        if (a[i][y] == 1)
            count++;
    if (count == N)
        return true;

    count = 0;
    for (int j = 0; j < M; j++)
        if (a[x][j] == 1)
            count++;
    if (count == M)
        return true;

    return false;
}

void solve() {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (a[i][j] == 1 && !isLegal(i, j)) {
                cout << "Case #" << nr_case << ": NO" << endl;
                return;
            }
    cout << "Case #" << nr_case << ": YES" << endl;
}

int main()
{
    int T;

    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    cin >> T;
    while (T--) {
        cin >> N >> M;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> a[i][j];
        solve();
        nr_case++;
    }
    return 0;
}
