#include <iostream>
#include <map>
#include <string>
using namespace std;

bool phone(std::map<int, int> input, string &ret) {
    static string strs[10] = {
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
        "EIGHT", "NINE"
    };
    if (input.size() == 0) {
        return true;
    }

    for (int i = 0; i < 10; i++) {
        bool contain = true;
        map<int, int> tmp = input;
        for (int j = 0; j < strs[i].size(); j++) {
            if (tmp.count(strs[i][j]) == 0) {
                contain = false;
                break;
            }
            tmp[strs[i][j]]--;
            if (tmp[strs[i][j]] == 0) {
                tmp.erase(strs[i][j]);
            }
        }
        if (contain == false) {
            continue;
        }
        string t = ret;
        ret += (i+'0');
        bool subret = phone(tmp, ret);
        if (subret == true) {
            return true;
        }
        ret = t;
    }
    return false;
}

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string s;
        cin >> s;
        std::map<int, int> input;
        for (int j = 0; j < s.size(); j++) {
            input[s[j]]++;
        }
        string number; 
        phone(input, number);
        cout << "Case #" << i <<": " << number << endl;
    }
    return 0;
}
