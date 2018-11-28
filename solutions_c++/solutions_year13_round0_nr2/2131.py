#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int a[100][100];

int main()
{
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        int n, m;
        cin >> n >> m;
        vector< pair<int, pair<int, int> > > v;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
                v.push_back(make_pair(a[i][j], make_pair(i, j)));
            }
        }

        sort(v.begin(), v.end());

        int i;
        for (i = 0; i < n * m; i++) {
            int y = v[i].second.first, x = v[i].second.second,
            d = v[i].first;

            bool was = false;
            bool isGood = true;
            for (int i = 0; i < m; i++)
                isGood &= (a[y][i] == d || a[y][i] < 0);

            was |= isGood;
            if (isGood) {
                for (int i = 0; i < m; i++)
                    a[y][i] = -1;
            }

            isGood = true;
            for (int i = 0; i < n; i++)
                isGood &= (a[i][x] == d || a[i][x] < 0);

            was |= isGood;
            if (isGood) {
                for (int i = 0; i < n; i++)
                    a[i][x] = -1;
            }
            if (!was) break;
        }

        cout << "Case #" << tc << ": " << (i == n * m ? "YES" : "NO") << endl;
    }

    return 0;
}
