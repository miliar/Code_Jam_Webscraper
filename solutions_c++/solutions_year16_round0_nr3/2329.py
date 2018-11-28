#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

string next_possible(string t) {
    int i = 2;
    t[t.length() - i]++;
    while(t[t.length() - i] == '2') {
        t[t.length() - i] = '0';
        t[t.length() - i - 1]++;
        i++;
    }
    return t;
}

unsigned long long numBase(string s, int base) {
    unsigned long long num = 0;
    for(int i = 0; i < s.length(); i++) {
        num += pow(base, s.length() - 1 - i) * (s[i]-'0');
    }
    return num;
}

int isPrime(unsigned long long num) {
    for(unsigned long long i = 2; i <= sqrt(num); i++) {
        if(num % i == 0)
            return i;
    }
    return -1;
}

int main() {
    fstream in("C-small-attempt0.in", ios::in);
    fstream out("coin.out", ios::out);
    int t, n, j;
    in >> t;
    in >> n;
    in >> j;
    int c = 0;
    string s(n, '0');
    s[0] = '1';
    s[n-1] = '1';
    vector<int> f;
    int temp;
    for(int cas = 1; cas <= t; cas++) {
        c = 0;
        out << "Case #" << cas << ": " <<endl;
        while(c != j) {
            f.clear();
            for(int i = 2; i <= 10; i++) {
                temp = isPrime(numBase(s, i));
                if(temp != -1) {
                    f.push_back(temp);
                }
                else {
                    break;
                }
            }
            if(f.size() == 9) {
                out << s << " ";
                for(int i = 0; i < f.size(); i++) {
                    out << f[i] << " ";
                }
                out << endl;
                c++;
            }
            s = next_possible(s);
        }

    }
    return 0;
}
