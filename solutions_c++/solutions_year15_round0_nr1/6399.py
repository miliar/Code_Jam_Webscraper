#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    int T;
    in >> T;
    for(int t = 1; t <= T; t++) {
        int smax;
        in >> smax;
        string s;
        in >> s;
        long total = 0;
        long ans = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s[i] > '0' && i > total) {
                ans += i - total;
                total += i - total;
            }
            total += s[i] - '0';
        }
        out << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
