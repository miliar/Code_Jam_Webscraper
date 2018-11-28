#include <iostream>
#include <string>
#include <bitset>
#include <stdlib.h>
#include <math.h>
#include <vector>

using namespace std;

void gen_01_str(vector<string> &ret, string cur_str, char cur_char, int len, int n) {
    
    if (cur_str.size() == len) {
        ret.push_back(cur_str);
        return;
    }

    if (cur_char == '0') {
        gen_01_str(ret, cur_str+"0", '0', len, n);
        if (ret.size() == n) return;
        gen_01_str(ret, cur_str+"1", '1', len, n);
        if (ret.size() == n) return;
    } else {
        gen_01_str(ret, cur_str+"0", '0', len, n);
        if (ret.size() == n) return;
    }
}

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    int len = 0, n = 0;
    cin >> len >> n;
    //"100....1 * 11"
    string prefix = "10";
    string suffix = "01";

    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ":" << endl;
        std::vector<string> collection;
        string cur = "0";
        gen_01_str(collection, cur, '0', len-5, n);
        for (int j = 0; j < n; j++) {
            char *ptr;
            string str = prefix + collection[j] + suffix;
            //cout << str << " ";
            //cout << collection[j];
            unsigned long long p = strtoull(str.c_str(), &ptr, 2);
            unsigned long long r = p * 3; // * "11"
            string dst = std::bitset<64>(r).to_string();
            dst = dst.substr(dst.find('1'));
            cout << dst;
            for (int base = 2; base <= 10; base++) {
                unsigned long long divisor = base + 1;
                cout << " " << divisor;
            }
            cout << endl;
        }
    }
    return 0;
}
