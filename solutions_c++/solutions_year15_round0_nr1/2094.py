#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int len;
string str;

bool doesWork(int e) {
    int standing = e;
    for (int i = 0; i < str.size(); ++i) {
        if (standing >= i) {
            standing += str[i] - '0';
        } else if (str[i] - '0' > 0) {
            return false;
        }
    }
    return true;
}

int bsearch() {
    int l = 0;
    int h = (len + 1) * 10;
    while (l < h) {
        int m = l + (h - l) / 2;
        if (doesWork(m)) {
            h = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

int main() {
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> len >> str;
        cout << "Case #" << (i + 1) << ": " << bsearch() << endl;
    }
}
