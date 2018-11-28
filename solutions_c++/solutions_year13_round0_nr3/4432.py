#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;

bool isFair(long long n) {
    stringstream ss;
    ss << n;
    string s = ss.str();
    int size = s.size();
    for (int i = 0; i != size/2; ++i) {
        if (s[i] != s[size-i-1]) {
            return false;
        }
    }
    return true;
}

int main (int argc, char const *argv[]) {
    int T, a, b;
    cin >> T;
    set<int> s;
    int num = 0;
    for (int i = 0; i != 32; ++i) {
        if (isFair(i)) {
            num = i*i;
            if (isFair(num)) {
                s.insert(num);
            }
        }
    }
    for (int t = 0; t != T; ++t) {
        cin >> a >> b;
        int count = 0;
        for (int i = a; i != b+1; ++i) {
            if (s.count(i) != 0) {
                ++count;
            }
        }
        cout << "Case #" << t+1 << ": " << count << endl;
    }
    return 0;
}
