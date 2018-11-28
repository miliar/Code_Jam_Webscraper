#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("./large.in", "r", stdin);
    freopen("./large.out", "w", stdout);

    int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        string temp;
        cin >> temp;
        
        //0 is sad, 1 is happy
        bool happy[temp.length()];
        for (int j=0; j<temp.length(); ++j) {
            if (temp[j] == '-') {
                happy[j] = false;
            }
            else if (temp[j] == '+') {
                happy[j] = true;
            }
        }

        int numblocks = 1;
        bool ishappy = happy[0];

        for (int j=1; j<temp.length(); ++j) {
            if (happy[j] != ishappy) {
                ishappy = happy[j];
                numblocks += 1;
            }
        }
        int answer = 2 * (numblocks / 2);
        if ((numblocks % 2) == 0) {
            if (!happy[0]) {
                answer = answer - 1;
            }
        }
        else {
            if (!happy[0]) {
                answer = answer + 1;
            }
        }

        cout << "Case #" << i << ": " << answer << "\n";
    }
    return 0;
}
