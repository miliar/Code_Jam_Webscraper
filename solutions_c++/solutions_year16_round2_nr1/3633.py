#include <iostream>
using namespace std;

const string forCounts[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
    "SIX", "SEVEN", "EIGHT", "NINE" };
int counts[10][26] = {}, curCounts[26], curDig[10], accCounts[26];

bool rec()
{
    bool same = true;
    for (int j = 0; j < 26; j++) {
        if (curCounts[j] != accCounts[j]) {
            same = false;
            break;
        }
    }
    if (same)
        return true;
    for (int i = 0; i < 10; i++) {
        bool possible = true;
        curDig[i]++;
        for (int j = 0; j < 26; j++) {
            curCounts[j] += counts[i][j];
            if (curCounts[j] > accCounts[j]) {
                possible = false;
            }
        }
        if (possible && rec())
            return true;
        curDig[i]--;
        for (int j = 0; j < 26; j++)
            curCounts[j] -= counts[i][j];
    }
    return false;
}

int main()
{
    int T;

    for (int i = 0; i < 10; ++i) {
        for (char c : forCounts[i])
            counts[i][c - 'A']++;
    }
    cin >> T;
    for (int t = 0; t < T; t++) {
        string S;
        cin >> S;
        for (int& i : curCounts)
            i = 0;
        for (int& i : curDig)
            i = 0;
        for (int& i : accCounts)
            i = 0;
        for (char c : S)
            accCounts[c - 'A']++;

        rec();
        cout << "Case #" << t + 1 << ": ";
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < curDig[i]; j++)
                cout << i;
        }
        cout << endl;
    }
    return 0;
}
