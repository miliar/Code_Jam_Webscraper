#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ifstream cin("A-large.in.txt");
    ofstream cout("A-large.out.txt");
    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q) {
        int n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << q << ": " << "INSOMNIA\n";
            continue;
        }
        vector<bool> seen(10, false);
        
        int to_see = 10;
        int cur = n;
        int last = n;
        while (to_see != 0) {
            last = cur;
            while(cur > 0) {
                if (!seen[cur % 10]) {
                    seen[cur % 10] = true;
                    --to_see;
                }
                cur /= 10;
            }
            cur = last + n;
        }
        cout <<  "Case #" << q << ": " << last << "\n";
    }
}
