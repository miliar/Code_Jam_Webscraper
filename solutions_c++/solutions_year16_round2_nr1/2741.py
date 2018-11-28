#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

string doit() {
    string s;

    getline(std::cin, s);

    int count[10] = {0};

    map<char, int> numberMap;

    for (int j = 0; j < 26; ++j) {
        numberMap[(char) 'A'+j]=0;
    }

    for (int i = 0; i < s.length(); ++i) {
        numberMap[s[i]]++;
    }

    // search for ZERO
    if (numberMap['Z'] > 0) {
        int zz = numberMap['Z'];

        count[0]+= zz;

        numberMap['Z'] -= zz;
        numberMap['E'] -= zz;
        numberMap['R'] -= zz;
        numberMap['O'] -= zz;
    }

    // search for TWO
    if (numberMap['W'] > 0) {
        int tt = numberMap['W'];

        count[2] += tt;

        numberMap['T'] -= tt;
        numberMap['W'] -= tt;
        numberMap['O'] -= tt;
    }

    // search for FOUR
    if (numberMap['U'] > 0) {
        int ff = numberMap['U'];

        count[4] += ff;

        numberMap['F'] -= ff;
        numberMap['O'] -= ff;
        numberMap['U'] -= ff;
        numberMap['R'] -= ff;
    }

    // search for SIX
    if (numberMap['X'] > 0) {
        int xx = numberMap['X'];

        count[6] += xx;

        numberMap['S'] -= xx;
        numberMap['I'] -= xx;
        numberMap['X'] -= xx;
    }

    // search for EIGHT
    if (numberMap['G'] > 0) {
        int gg = numberMap['G'];

        count[8] += gg;

        numberMap['E'] -= gg;
        numberMap['I'] -= gg;
        numberMap['G'] -= gg;
        numberMap['H'] -= gg;
        numberMap['T'] -= gg;
    }

    // search for ONE
    if (numberMap['O'] > 0) {
        int oo = numberMap['O'];

        count[1] += oo;

        numberMap['O'] -= oo;
        numberMap['N'] -= oo;
        numberMap['E'] -= oo;
    }

    // search for THREE
    if (numberMap['H'] > 0) {
        int tt = numberMap['H'];

        count[3] += tt;

        numberMap['T'] -= tt;
        numberMap['H'] -= tt;
        numberMap['R'] -= tt;
        numberMap['E'] -= tt;
        numberMap['E'] -= tt;
    }

    // search for FIVE
    if (numberMap['F'] > 0) {
        int vv = numberMap['F'];

        count[5] += vv;

        numberMap['F'] -= vv;
        numberMap['I'] -= vv;
        numberMap['V'] -= vv;
        numberMap['E'] -= vv;
    }

    // search for SEVEN
    if (numberMap['S'] > 0) {
        int ee = numberMap['S'];

        count[7] += ee;

        numberMap['S'] -= ee;
        numberMap['E'] -= ee;
        numberMap['V'] -= ee;
        numberMap['E'] -= ee;
        numberMap['N'] -= ee;
    }

    count[9] = numberMap['I'];

    string phoneNumber = "";

    for (int k = 0; k < 10; ++k) {
        if (count[k] > 0) {
            for (int i = 0; i < count[k]; ++i) {
                phoneNumber += '0' + k;
            }
        }
    }

    return phoneNumber;
}

int main() {

    int t;

    cin >> t;

    string tmp;

    getline(std::cin, tmp);

    for (int i = 0; i < t; ++i) {
        string res = doit();

        printf("Case #%d: %s\n", i+1, res.c_str());
    }

    return 0;
}