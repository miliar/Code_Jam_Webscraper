#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int t, k;
    int a, b;
    int s[4], s1[4];
    cin >> t;
    for (int g = 1; g <= t; g++) {
        cin >> a;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> k;
                if (i == a-1) {
                    s[j] = k;
                }
            }
        }
        cin >> b;
                for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> k;
                if (i == b-1) {
                    s1[j] = k;
                }
            }
        }

        int count = -1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0 ; j < 4; j++) {
                if (s[i] == s1[j]) {
                    if (count == -1)
                        count = s[i];
                    else {
                        count = -2;
                        break;
                    }
                }
            }
        }

        cout << "Case #" << g << ": ";
        if (count == -1) {

            cout << "Volunteer cheated!\n";
        } else if (count == -2) {
            cout << "Bad magician!\n";
        } else {
            cout << count << endl;
        }
    }
    return 0;
}
