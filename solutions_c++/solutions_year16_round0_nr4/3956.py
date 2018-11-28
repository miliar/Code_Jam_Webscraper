#include <fstream>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int k, c, s;
        in >> k >> c >> s;
        out << "Case #" << tt + 1 << ": ";
        if(s < (k + c - 1) / c) {
            out << "IMPOSSIBLE\n";
            continue;
        }
        s = (k + c - 1) / c;
        int pos = 0;
        for(int i = 0; i < s; i++) {
            long long x = 0;
            for(int j = 0; j < c; j++) {
                x = x * k + pos;
                if(pos < k - 1)
                    pos++;
            }
            out << x + 1 << ' ';
        }
        out << '\n';
    }
    return 0;
}
