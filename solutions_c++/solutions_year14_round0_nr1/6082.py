#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

void comeAndPlay()
{
    int x1[5][5], x2[5][5], m1, m2;

    cin >> m1;

    for (int k = 1; k <= 4; k++)
        for (int j = 1; j <= 4; j++)
            cin >> x1[k][j];

    cin >> m2;

    for (int k = 1; k <= 4; k++)
        for (int j = 1; j <= 4; j++)
            cin >> x2[k][j];

    int flow[17];
    memset(flow, 0, sizeof(flow));

    for (int k = 1; k <= 4; k++)
        flow[x1[m1][k]]++;
    for (int k = 1; k <= 4; k++)
        flow[x2[m2][k]]++;

    int lol = -1;
    bool duplicate = false;
    for (int k = 1; k <= 16; k++) {
        if (flow[k] == 2) {
            if (lol == -1) {
                lol = k;
            } else {
                duplicate = true;
                break;
            }
        }
    }

    if (duplicate == true) {
        cout << "Bad magician!";
        return;
    }

    if (lol == -1) {
        cout << "Volunteer cheated!";
    } else {
        cout << lol;
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    for (int k = 1; k <= n; k++) {
        cout << "Case #" << k << ": ";
        comeAndPlay();
        cout << endl;
    }

    return 0;
}

