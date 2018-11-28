#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        int k;
        in >> s >> k;
        int cnt = 0;
        for (int j = 0; j < s.size(); ++j)
            if (s[j] == '-') {
                if (j + k <= s.size()) {
                    for (int l = j; l < j + k; ++l)
                        s[l] = s[l] == '-' ? '+' : '-';
                    ++cnt;
                }
                else {
                    cnt = -1;
                    break;
                }
            }
        out << "Case #" << i + 1 << ": ";
        if (cnt == -1)
            out << "IMPOSSIBLE\n";
        else
            out << cnt << '\n';
    }
}
