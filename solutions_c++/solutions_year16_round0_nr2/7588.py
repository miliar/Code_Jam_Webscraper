#include <iostream>
#include <fstream>
#include <climits>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

typedef unsigned long long int64;
ifstream in("/Users/msiddeek/workspace/algorithms/input.txt");
ofstream out("/Users/msiddeek/workspace/algorithms/output.txt");

int main() {
    int64 T;
    in >> T;
    for (int64 i = 0; i < T; ++i) {
        string S;
        in >> S;
        int64 ans = 0;
        for (int j = 1; j < S.length(); ++j)
            if (S[j] != S[j - 1])
                ans++;
        ans += (S[0] == '+' ? ans % 2 : (1 - (ans % 2)));
        out << "Case #" << (i + 1) << ": " << ans << endl;
    }
    return 0;
}