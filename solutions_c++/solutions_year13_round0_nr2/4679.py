#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int ntests;

    cin >> ntests;

    for (int test = 0; test < ntests; ++test) {
        int n, m;
        scanf("%d %d", &n, &m);

        vector<vector<int> > field(n, vector<int> (m, 0));
        vector<vector<int> > tfield(m, vector<int> (n, 0));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int elem;
                scanf("%d", &elem);
                field[i][j] = elem;
                tfield[j][i] = elem;
            }
        }
//////////////////////
        vector<int> rowmax(n, 0);
        vector<int> colmax(m, 0);
        
        for (int i = 0; i < n; ++i) {
            rowmax[i] = *max_element(field[i].begin(), field[i].end());
        }

        for (int j = 0; j < m; ++j) {
            colmax[j] = *max_element(tfield[j].begin(), tfield[j].end());
        }

        string answer = "YES";

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (field[i][j] != rowmax[i] && field[i][j] != colmax[j]) {
                    answer = "NO";
                    break;
                }
            }
        }

        printf("Case #%d: %s\n", test + 1, answer.c_str());
    }

    return 0;
}
