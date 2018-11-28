#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

#include <cmath>

ifstream inf("Input.txt");
ofstream outf("Output.txt");

typedef long long LL;

const int sp[39] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};


bool is_pal(LL n) {
    string s = "";
    while (n > 0) {
        s += n%10 + '0';
        n /= 10;
    }
    string rs = s;
    reverse(rs.begin(), rs.end());
    return rs == s;
}

int main() {
    int T;
    inf >> T;
    for (int tc = 1; tc <= T; tc++) {
        outf << "Case #" << tc << ": ";
        LL A, B;
        inf >> A >> B;
        int start = sqrt(A);
        while ((LL)start*start < A) ++start;
        int ans = 0;
        for (int i = 0; i < 39; i++) {
            if ((LL)sp[i]*sp[i] >= A && (LL)sp[i]*sp[i] <= B)
                ++ans;
        }
        /*for (int i = start; (LL)i*i <= B; i++)
            if (is_pal(i) && is_pal((LL)i*i)) {
                outf << i << ", ";
                ++ans;
            }
            */
        outf << ans << "\n";
    }
}
