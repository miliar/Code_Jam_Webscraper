#include<iostream>
#include<bitset>
#include <vector>
#include <string>
#include <cstddef>

using namespace std;

int isNotPrime(unsigned long long int num) {
    if(!(num % 2))
        return 2;
    for(int i = 3; i * i <= num; i += 2)
        if(!(num % i))
            return i;
    return 0;
}

unsigned long long int baseToTen(string & str, int base) {
    unsigned long long int tmp = 1, num = 0;
    for(int i = str.size() - 1; i >= 0; i--) {
        num += (str[i] - '0') * tmp;
        tmp *= base;
    }
    return num;
}

int main() {
    int nCase, xC = 1;
    cin >> nCase;
    while(nCase--) {
        cout << "Case #" << xC++ << ":" << endl;
        int si, n, iTillNow = 0;
        cin >> si >> n;
        bool finished = false;
        for(int i = 0; i <= (1 << (n - 1)) - 1; i++) {
            vector<int> vec;
            bitset<32> b(0);
            b[0] = 1; b[si - 1] = 1;
            b |= (i << 1);
            string str = b.to_string();
            str = str.substr(32 - si);
            int devisor;
            for(int i = 2; i <= 10; i++) {
                if (!(devisor = isNotPrime(baseToTen(str, i))))
                    break;
                vec.push_back(devisor);
                if(i == 10) {
                    cout << str;
                    for(int j = 0; j < 9; j++)
                        cout << " " << vec[j];
                    cout << endl;
                    iTillNow++;
                }
                if(iTillNow == n) {
                    finished = true;
                    break;
                }
            }
            if(finished)
                break;
        }
    }

    return 0;
}