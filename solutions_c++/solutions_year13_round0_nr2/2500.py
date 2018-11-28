#include <iostream>
#include <limits>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int N, M;

bool query(const VVI& lawn, const VI& max_row, const VI& max_col)
{
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            if (lawn[i][j] < max_row[i] && lawn[i][j] < max_col[j])
                return false;

    return true;
}

int main()
{
    int T;
    cin >> T;

    for (int k = 1; k <= T; ++k) {
        cin >> N >> M;

        VVI lawn(N, VI(M));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                cin >> lawn[i][j];

        cout << "Case #" << k << ": ";

        VI max_row(N, numeric_limits<int>::min());
        VI max_col(M, numeric_limits<int>::min());

        for (int i = 0; i < N; ++i) 
            for (int j = 0; j < M; ++j) {
                max_row[i] = max(max_row[i], lawn[i][j]);
                max_col[j] = max(max_col[j], lawn[i][j]);
            }

        if (query(lawn, max_row, max_col))
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
