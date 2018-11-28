#include<iostream>
#include<string>
#include<vector>
#include<iterator>
#include<set>
#include<algorithm>
#include<map>
using namespace std;

const string d2s[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

string s;
vector<int> nums;

void removeD(int d) {
    auto dstr = d2s[d];
    map<char, int> ms;
    for (int i=0; i < dstr.size(); i++) {
        char c = dstr[i];
        ms[c] = ms[c] + 1;
    }
    int count = 0;
    for (int i=0; i < s.size() && count < dstr.size(); i++) {
        char c = s[i];
        if (ms[c] != 0) {
            ms[c] -= 1;
            count++;
            s[i] = '?';
        }
    }
}

void number() {
    // zero, two, four, six
    for(int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == 'Z') {
            nums.push_back(0);
            removeD(0);
        } else if (c == 'W') {
            nums.push_back(2);
            removeD(2);
        } else if (c == 'U') {
            nums.push_back(4);
            removeD(4);
        } else if (c == 'X') {
            nums.push_back(6);
            removeD(6);
        }
    }

    // five, seven
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == 'F') {
            nums.push_back(5);
            removeD(5);
        } else if (c == 'S') {
            nums.push_back(7);
            removeD(7);
        }
    }


    // three, one
    for (int i=0; i < s.size(); i++) {
        char c = s[i];
        if (c == 'R') {
            nums.push_back(3);
            removeD(3);
        } else if (c == 'O') {
            nums.push_back(1);
            removeD(1);
        }
    }


    // eight
    for (int i=0; i < s.size(); i++) {
        char c = s[i];
        if (c == 'T') {
            nums.push_back(8);
            removeD(8);
        }
    }


    // nine
    for (int i=0; i < s.size(); i++) {
        char c = s[i];
        if (c != '?') {
            nums.push_back(9);
            removeD(9);
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        nums.clear();
        number();
        sort(nums.begin(), nums.end());
        cout << "Case #" << i << ": ";
        for (auto it = nums.begin(); it != nums.end(); it++) {
            cout << *it;
        }
        cout << endl;
    }
}
