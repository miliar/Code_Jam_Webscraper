#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdint>

using namespace std;

/*
string to_str(uint64_t num) {
    stringstream ss; ss << num;
    return ss.str();
}

bool palindromic(const string& str) {
    for (int i = 0, j = str.size() / 2; i != j; ++i)
        if (str[i] != str[j - i - 1]) return false;
    return true;
}*/

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    int stuff[] = {
        1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 698896
	};
    for (int cas = 1; cas <= cases; ++cas) {
        int a, b;
        cin >> a >> b;
		cout << "Case #" << cas << ": " << (upper_bound(begin(stuff), end(stuff), b) - lower_bound(begin(stuff), end(stuff), a)) << "\n";
	}
}
