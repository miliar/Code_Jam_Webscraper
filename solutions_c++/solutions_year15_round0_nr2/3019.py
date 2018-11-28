#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ifstream inf("B-large.in");
    ofstream outf("output.txt");

    int T; inf >> T;
    for (int t = 1; t <= T; t++) {
        outf << "Case #" << t << ": ";
        int D; inf >> D;
        vector<int> p(D);
        int mp = -1;
        for (int i = 0; i < D; i++) {
            inf >> p[i];
            if (mp == -1 || mp < p[i]) mp = p[i];
        }
        int ans = mp;
        for (int s = 1; s < mp; s++) {
            int curr = s;
            for (int i = 0; i < D; i++) {
                curr += p[i] / s;
                if (p[i] > 0 && p[i] % s == 0) --curr;
            }
            if (ans == -1 || curr < ans) {
                ans = curr;
            }
        }
        outf << ans << "\n";
    }
}

