#include <bits/stdc++.h>

using namespace std;

ifstream in;
ofstream out;

const int MAXN = 1001;

vector < vector <int> > dp;

int rec(int x, int y) {
   return dp[x][y];
}

void init() {
    dp.resize(MAXN + 1, vector <int>(MAXN + 1, 0));

    for (int i = 1; i <= MAXN; i++) {
        for (int j = 1; j < i; j++) {
            if (i <= j) {
                dp[i][j] = 0;
            }
            else {
                dp[i][j] = 1 + dp[i - 1][j];
                for (int k = 2; k <= j; k++) {
                    dp[i][j] = min(dp[i][j], dp[i - k][j] + 1);
                }
            }
        }
    }
}

int solve() {

    int d; in >> d;
    vector <int> p(d, 0);

    for (int i = 0; i < d; i++) {
        in >> p[i];
    }

    int result = MAXN;

    for (int i = 1; i <= MAXN; i++) {
        int current_result = i;
        for (int j = 0; j < d; j++) {
            current_result += rec(p[j], i);
        }
        result = min(result, current_result);
    }

    return result;
}

int main() {

    in.open("C:\\Users\\Alex\\ClionProjects\\GoogleCodeJam\\input.txt");
    out.open("C:\\Users\\Alex\\ClionProjects\\GoogleCodeJam\\output.txt");

    init();

    int t; in >> t;

    for (int i = 0; i < t; i++)  {
        int result = solve();
        out << "Case #" << i + 1 << ": " << result << endl;

    }

    return 0;
}