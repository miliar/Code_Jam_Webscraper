#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

bool isEqual(const vector<int>& parties)
{
    int sum = 0, n = parties.size();

    for (int i = 0; i < n; ++i) {
        sum += parties[i];
    }

    for (int i = 0; i < n; ++i) {
        if (sum < parties[i] * 2) return false;
    }

    return true;
}

int sum = 0;

void outParties(int first, int second = -1)
{
    sum--;
    cout << " " << char('A' + first);
    if (second != -1) {
        sum--;
        cout << char('A' + second);
    }
}



int main()
{
    int T;
    cin >> T;

    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(6);

    for (int test = 1; test <= T; ++test) {

        vector<int> parties;
        int n;
        cin >> n;

        for (int i = 0; i < n; ++i) {
            int d;
            cin >> d;
            parties.push_back(d);
        }

        sum = 0;
        for (int i = 0; i < parties.size(); ++i) {
            sum += parties[i];
        }

        cout << "Case #" << test << ":";

        while (sum) {
            bool go = true;

            for (int i = 0; i < n; ++i) {
                parties[i]--;
                if (isEqual(parties)) {
                    outParties(i);
                    go = false;
                    break;
                }
                else {
                    parties[i]++;
                }
            }

            for (int i = 0; i < n && go; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    parties[i]--;
                    parties[j]--;
                    if (isEqual(parties)) {
                        outParties(i, j);
                        go = false;
                        break;
                    }
                    else {
                        parties[i]++;
                        parties[j]++;
                    }
                }
            }
        }

        cout << endl;
    }

    return 0;
}
