#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

vector<string> digits = {"ZERO", "TWO", "SIX", "EIGHT", "SEVEN", "FIVE", "NINE", "THREE", "FOUR", "ONE"};
vector<int> m = {0, 2, 6, 8, 7, 5, 9, 3, 4, 1};

bool poss(const string &s, vector<int> letters) {
    for(const char &c : s) {
        if(letters[c - 'A'] == 0) return false;
        letters[c - 'A']--;
    }
    return true;
}

void red(const string &s, vector<int> &letters) {
    for(const char &c : s) letters[c - 'A']--;
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string S;
        cin >> S;
        vector<int> letters(26);
        multiset<int> res;
        for(const char &c : S) letters[c - 'A']++;
        for(int i = 0; i < 10; i++) {
            while(poss(digits[i], letters)) res.insert(m[i]), red(digits[i], letters);
        }
        cout << "Case #" << t << ": ";
        for(const int &i : res) cout << i;
        cout << endl;
    }
    return 0;
}
