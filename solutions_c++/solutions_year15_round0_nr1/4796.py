#include <iostream>
#include <cstdio>

using namespace std;

#define MAX 1005

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdin);

    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int maxS, testCase;
    char str[MAX];

    cin >> testCase;

    for (int kase = 1; kase <= testCase; kase++) {
        cin >> maxS >> str;

        int invited = 0;
        int soFar = 0;

        for (int i = 0; i <= maxS; i++) {
            if (soFar < i) {
                invited += (i - soFar);
                soFar += (i - soFar);
            }

            soFar += (str[i] - '0');
        }

        cout << "Case #" << kase << ": " << invited << "\n";
    }

    return 0;
}
