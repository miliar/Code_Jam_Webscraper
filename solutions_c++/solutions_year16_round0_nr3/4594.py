#include <iostream>
#include <string>
#include <bitset>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool add_one(string &src) {
    int n = src.size();
    int c = 1;
    for (int i = n-1; i >= 0; i--) {
        int r = src[i] - '0' + c;
        src[i] = (r % 2) + '0';
        c = r >= 2 ?1 :0;
        if (c == 0) break;
    }
    return (c == 0);
}

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    int len = 0, n = 0;
    cin >> len >> n;
    //"100....1 * 11"
    string prefix = "10";
    string suffix = "01";
    string middle;
    string str;
    for (int i = 5; i < len; i++) {
        middle.append("0");
    }
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ":" << endl;
        int count = 0;
        while (count < 50) {
            char *ptr;
            str = prefix + middle + suffix;
            long p = strtol(str.c_str(), &ptr, 2);
            long r = p * 3; // * "11"
            string dst = std::bitset<64>(r).to_string();
            dst = dst.substr(dst.find('1'));
            bool find = true;
            for (int base = 2; base <= 10; base++) {
                int divisor = base + 1;
                long tmp = 0;
                int po = 0;
                for (int l = dst.size() - 1; l >= 0; l--) {
                    tmp += (dst[l] - '0') * pow(base, po);
                    po++;
                }
                if (tmp % divisor != 0) {
                    find = false;
                    break;
                }
            }
            if (find) {
                cout << dst;
                for (int base = 2; base <= 10; base++) {
                    cout << " " << base+1;
                }
                cout << endl;
                count++;
            }
            add_one(middle);
        }
    }
    return 0;
}
