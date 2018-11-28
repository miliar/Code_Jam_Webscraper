#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <sstream>
#include <cmath>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <algorithm>

using namespace std;

typedef long long ll;

string shorten(string s) {
    string ret = "";
    for (int i = 0; i < s.size(); i++) {
        if (i != 0 && s[i] == s[i - 1]) {
            continue;
        }
        ret.append(1, s[i]);
    }
    return ret;
}

int minOps(string s) {
    string ret = shorten(s);
    for (int i = ret.size() - 1; i >= 0; i--) {
        if (ret[i] == '-') {
            return i + 1;
        }
    }
    // all '+' case
    return 0;
}

int main() {
    string file_path = "C:\\Users\\Aidan\\Desktop\\jam\\input.in";
    ifstream data (file_path.c_str(), ios::in);
    ofstream ret ("C:\\Users\\Aidan\\Desktop\\jam\\output.out");
    int T;
    data >> T;
    string s;

    for (int round = 1; round <= T; round++) {
        data >> s;
        ret << "Case #" << round << ": " << minOps(s) << endl;
    }
    ret.close();
    return 0;
}
