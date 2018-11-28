#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int T;
    string P;
    cin >> T;
    map<char,int> number;
    vector<int> phone;
for(int kase = 1; kase <= T; ++kase) {
    number.clear();
    phone.clear();
    cin >> P;
    int sz = (int)P.size();
    for(int i = 0; i < sz; i++) {
        number[P[i]] += 1;
    }
    while(sz > 0) {
        if(number['Z'] > 0) {
            number['Z']-=1;
            number['E']-=1;
            number['R']-=1;
            number['O']-=1;
            sz -= 4;
            phone.push_back(0);
            continue;
        }
        if(number['W'] > 0) {
            number['T']-=1;
            number['W']-=1;
            number['O']-=1;
            sz -= 3;
            phone.push_back(2);
            continue;
        }
        if(number['X'] > 0) {
            number['S']-=1;
            number['I']-=1;
            number['X']-=1;
            sz -= 3;
            phone.push_back(6);
            continue;
        }
        if(number['U'] > 0) {
            number['F']-=1;
            number['O']-=1;
            number['U']-=1;
            number['R']-=1;
            sz -= 4;
            phone.push_back(4);
            continue;
        }
        if(number['F'] > 0) {
            number['F']-=1;
            number['I']-=1;
            number['V']-=1;
            number['E']-=1;
            sz -= 4;
            phone.push_back(5);
            continue;
        }
        if(number['V'] > 0) {
            number['S']-=1;
            number['E']-=1;
            number['V']-=1;
            number['E']-=1;
            number['N']-=1;
            sz -= 5;
            phone.push_back(7);
            continue;
        }
        if(number['G'] > 0) {
            number['E']-=1;
            number['I']-=1;
            number['G']-=1;
            number['H']-=1;
            number['T']-=1;
            sz -= 5;
            phone.push_back(8);
            continue;
        }
        if(number['H'] > 0) {
            number['T']-=1;
            number['H']-=1;
            number['R']-=1;
            number['E']-=1;
            number['E']-=1;
            sz -= 5;
            phone.push_back(3);
            continue;
        }
        if(number['I'] > 0) {
            number['N']-=1;
            number['I']-=1;
            number['N']-=1;
            number['E']-=1;
            sz -= 4;
            phone.push_back(9);
            continue;
        }
            number['O']-=1;
            number['N']-=1;
            number['E']-=1;
            sz -= 3;
            phone.push_back(1);
    }
    sort(phone.begin(),phone.end());
    cout << "Case #" << kase << ": ";
    for(int i = 0; i < (int)phone.size(); ++i)
        cout << phone[i];
    cout << endl;
}
    return 0;
}
