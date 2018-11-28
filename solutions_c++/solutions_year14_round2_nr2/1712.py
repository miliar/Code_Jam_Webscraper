#include <fstream>
#include <set>
using namespace std;

ifstream in("input-a.txt");
ofstream out("output-a.txt");

int main() {
    int t;
    in >> t;
    for (int tt = 0; tt < t; tt++) {
        int a, b, k, ans = 0;
        in >> a >> b >> k;
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k) {
                    ans++;
                }
            }
        }
        out << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return 0;
}
