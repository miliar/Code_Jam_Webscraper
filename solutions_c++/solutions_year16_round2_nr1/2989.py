#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

int memo[10][26];

bool solve(vector<int> counts, vector<int> &l) {
    bool check = true;
    for (int i = 0; i < 26; ++i) {
        if (counts[i] != 0) {
            check = false;
        }
    }
    if (check) {
        return true;
    }

    for (int i = 0; i < 10; i++) {
        auto c = counts;
        for (int j = 0; j < 26; j++) {
            c[j] -= memo[i][j];
            if (c[j] < 0) {
                goto next;
            }
        }
        l.push_back(i);
        if (solve(c, l)) {
            return true;
        }
        l.pop_back();
        next:
//        cerr << "-----------------" << endl;
//        for (int i = 0; i < 26; ++i) {
//            cerr << static_cast<char>('A' + i) << ": " << counts[i] << ", ";
//        }
//        cerr << endl;
//        cerr << "-----------------" << endl;
        ;
    }
    return false;
}

string solve(string S) {
    vector<int> counts;
    for (int i = 0; i < 26; ++i) {
        counts.push_back(0);
    }
    for (int i = 0, l = S.size(); i < l; i++) {
        counts[S[i] - 'A']++;
    }

//    cerr << "-----------------" << endl;
//    for (int i = 0; i < 26; ++i) {
//        cerr << static_cast<char>('A' + i) << ": " << counts[i] << ", ";
//    }
//    cerr << endl;
//    cerr << "-----------------" << endl;

    vector<int> l;

    // 0
    if (counts['Z' - 'A']) {
        for (int i = 0, len = counts['Z' - 'A']; i < len; i++) {
            l.push_back(0);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[0][j];
            }
        }
    }
    // 2
    if (counts['W' - 'A']) {
        for (int i = 0, len = counts['W' - 'A']; i < len; i++) {
            l.push_back(2);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[2][j];
            }
        }
    }
    // 4
    if (counts['U' - 'A']) {
        for (int i = 0, len = counts['U' - 'A']; i < len; i++) {
            l.push_back(4);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[4][j];
            }
        }
    }
    // 6
    if (counts['X' - 'A']) {
        for (int i = 0, len = counts['X' - 'A']; i < len; i++) {
            l.push_back(6);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[6][j];
            }
        }
    }
    // 8
    if (counts['G' - 'A']) {
        for (int i = 0, len = counts['G' - 'A']; i < len; i++) {
            l.push_back(8);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[8][j];
            }
        }
    }

    // 3
    if (counts['H' - 'A']) {
        for (int i = 0, len = counts['H' - 'A']; i < len; i++) {
            l.push_back(3);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[3][j];
            }
        }
    }
    // 5
    if (counts['F' - 'A']) {
        for (int i = 0, len = counts['F' - 'A']; i < len; i++) {
            l.push_back(5);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[5][j];
            }
        }
    }

    // 9
    if (counts['I' - 'A']) {
        for (int i = 0, len = counts['I' - 'A']; i < len; i++) {
            l.push_back(9);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[9][j];
            }
        }
    }

    // 1
    if (counts['O' - 'A']) {
        for (int i = 0, len = counts['O' - 'A']; i < len; i++) {
            l.push_back(1);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[1][j];
            }
        }
    }

    // 7
    if (counts['N' - 'A']) {
        for (int i = 0, len = counts['N' - 'A']; i < len; i++) {
            l.push_back(7);
            for (int j = 0; j < 26; j++) {
                counts[j] -= memo[7][j];
            }
        }
    }

//    cerr << "-----------------" << endl;
//    for (int i = 0; i < 26; ++i) {
//        cerr << static_cast<char>('A' + i) << ": " << counts[i] << ", ";
//    }
//    cerr << endl;
//    cerr << "-----------------" << endl;

    assert(solve(counts, l));

    sort(l.begin(), l.end());

    string answer;
    for (auto e : l) {
        answer.push_back(static_cast<char>(e + '0'));
    }
    return answer;
}

int main() {
    for (int i = 0; i < 10; i++) {
        string d;
        switch (i) {
            case 0: d = "ZERO"; break;
            case 1: d = "ONE"; break;
            case 2: d = "TWO"; break;
            case 3: d = "THREE"; break;
            case 4: d = "FOUR"; break;
            case 5: d = "FIVE"; break;
            case 6: d = "SIX"; break;
            case 7: d = "SEVEN"; break;
            case 8: d = "EIGHT"; break;
            case 9: d = "NINE"; break;
        }
        for (int j = 0; j < d.size(); j++) {
            memo[i][d[j] - 'A']++;
        }
//    cerr << i << ":: ";
//    for (int j = 0; j < 26; ++j) {
//        cerr << static_cast<char>('A' + j) << ": " << memo[i][j] << ", ";
//    }
//    cerr << endl;
    }
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string S;
        cin >> S;
        cout << "Case #" << t + 1 << ": " << solve(S) << endl;
    }
    return 0;
}