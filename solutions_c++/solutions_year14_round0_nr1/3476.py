#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int c[100];
int a;
int n;
int x;

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ": ";
        for (int i = 0; i < 50; i++) c[i] = 0;
        for (int qq = 0; qq < 2; qq++) {
            cin >> x;
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++) {
                    cin >> a;
                    if (i+1 == x) c[a]++;
                }
        }
        int cnt = 0, ans = -1;
        for (int i = 1; i <= 16; i++)
            if (c[i] == 2) cnt++, ans = i;
        if (cnt == 0) cout << "Volunteer cheated!\n";
        else if (cnt > 1) cout << "Bad magician!\n";
        else cout << ans << endl;
    }

    return 0;
}
