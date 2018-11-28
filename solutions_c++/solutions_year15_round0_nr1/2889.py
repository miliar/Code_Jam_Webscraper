#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("result-large.out");


int main() {
    int t, n, cases = 1;
    string str;
    fin >> t;
    while (t--) {
        fin >> n >> str;
        int cnt = 0;
        int res = 0;
        for (int i = 0; i < str.length(); ++i) {
            cnt = cnt + (str[i] - '0');
            if (cnt < i + 1) {
                ++res;
                ++cnt;
            }
        }
        fout << "Case #" << cases++ << ": " << res << endl;
    }

	return 0;
}
