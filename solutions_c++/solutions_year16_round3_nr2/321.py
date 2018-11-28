#include <fstream>
#include <iostream>
#include <string>
#include <cmath>

#define BUFSIZE 1000

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int tests;
    char buf[BUFSIZE];

    int n;
    long long m;
    int a[50][50];

    cin >> tests;
    cin.getline(buf, BUFSIZE);

    for (int t = 0; t < tests; t++) {

        cin >> n >> m;

        cout << "Case #" << t+1 << ": ";
        if (log2(m) > n - 2) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = 0;
            }
        }

        long long full_part = (int)log2(m);
        m -= (long long)pow(2, full_part);
        for (int i = 0; i <= full_part+1; i++) {
            for (int j = i + 1; j <= full_part+1; j++) {
                a[i][j] = 1;
            }
        }

        if (full_part+1 < n-1) {
            a[full_part+1][n-1] = 1;
        }
        long long tail = (long long)pow(2, full_part-1);
        int cur_v = full_part;
        while (m > 0) {
            if (m >= tail) {
                m -= tail;
                a[cur_v][n-1] = 1;
            }
            cur_v--;
            tail /= 2;
        }

        cout << "POSSIBLE" << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << a[i][j];
            }
            cout << endl;
        }

    }

    cin.close();
    cout.close();

    return 0;
}
