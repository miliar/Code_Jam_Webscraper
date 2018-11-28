#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;


int main()
{
    int T, n;
    string str;
    ifstream fin("A-large.in");
    ofstream fout("ans.txt");
    fin >> T;
    for (int i = 1; i <= T; ++i) {
        fin >> n >> str;
        int ans = 0, val = str[0] - '0';
        for (int j = 1; j <= n; ++j) {
            if (val < j) {
                ans += j - val;
                val += j - val;
            }
            val += str[j] - '0';
        }
        fout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
