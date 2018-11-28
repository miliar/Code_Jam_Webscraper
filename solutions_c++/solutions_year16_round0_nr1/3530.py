#include <fstream>
#include <bitset>

using namespace std;

typedef long long ll;

ifstream cin("in");
ofstream cout("out");

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        ll n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << i + 1 << ": INSOMNIA\n";
            continue;
        }
        ll yet = 0;
        ll c = 0;
        while (yet != (1 << 10) - 1) {
            c += n;
            string s = to_string(c);
            for (char c: s) {
                yet |= 1 << (c - '0');
            }
        }
        cout << "Case #" << i + 1 << ": " << c << '\n';
    }
}
