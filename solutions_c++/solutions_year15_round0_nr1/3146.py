#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream inf("A-large.in");
    ofstream outf("output.txt");

    int T; inf >> T;
    for (int t = 1; t <= T; t++) {
        outf << "Case #" << t << ": ";
        int max_s; inf >> max_s;
        string s; inf >> s;
        int ans = 0;
        int curr = s[0] - '0';
        for (int i = 1; i < s.length(); i++) {
            if (curr < i) {
                ans += i - curr;
                curr = i;
            }
            curr += s[i] - '0';
        }
        outf << ans << "\n";
    }
}

