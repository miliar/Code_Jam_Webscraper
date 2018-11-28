#include <iostream>
#include <map>
#include <string>
using namespace std;

string phone(std::map<int, int> input) {
    static string strs[10] = {
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
        "EIGHT", "NINE"
    };
    
    char c[10] = {
        'Z','W', 'U','X','G','O','R','F','S','E'
    };
    int idx[10] = {
        0,2,4,6,8,1,3,5,7,9
    };

    int r[10] = {0};

    for (int i = 0; i < 10; i++) {
        char t = c[i];
        int index = idx[i];

        if (input[t] == 0) {
            r[index] = 0;
        } else {
            r[index] = input[t];
            string tmp = strs[index];
            for (int j = 0; j < tmp.size(); j++) {
                input[tmp[j]] -= r[index];
            }
        }
    }
    string ret;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < r[i]; j++) {
            ret.push_back(i+'0');
        }
    }
    return ret;
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
        cout << "Case #" << i <<": " << phone(input) << endl;
    }
    return 0;
}
