#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

int d;
int p[1005];

inline int f (int n, int k) {
    return (n + k) / (k + 1);
}

inline bool works (int specials, int h) {
    int where = 0;
    int sum = 0;

    for (int i = 1; i <= d; i++) {
        while (where + 1 < p[i] && f(p[i], where) > h)
            where ++;

        sum += where;
    }

    return (sum <= specials);
}

inline int solve (int specials) {
    int left = 1;
    int right = 1000;
    int mijl = 500;
    int ans = ((left + right) >> 1);

    while (left <= right) {
        if (works(specials, mijl)) {
            ans = mijl;
            right = mijl - 1;
        }
        else
            left = mijl + 1;

        mijl = ((left + right) >> 1);
    }

    return ans;
}

int main()
{
    ifstream cin("large.in");
    ofstream cout("large.out");

    int t = 0;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cin >> d;

        for (int j = 1; j <= d; j++)
            cin >> p[j];
        sort (p + 1, p + d + 1);

        int best = 1010, aux;
        for (int j = 0; j <= 1005; j++) {
            aux = j + solve(j);

            if (aux < best)
                best = aux;
        }

        cout << "Case #" << i << ": " << best << '\n';
    }

    cin.close();
    cout.close();
    return 0;
}
