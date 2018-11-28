#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int Smax;
        cin >> Smax;
        int i = 0, cur = 0, invited = 0;
        while (i<=Smax){
            int k;
            scanf("%1d", &k);
            if (k == 0) {
                ++i;
                continue;
            }
            if (i <= cur){
                cur += k;
            }
            else{
                invited += (i - cur);
                cur = i + k;
            }
            ++i;
        }
        cout << "Case #" << t << ": " << invited << endl;
    }
    return 0;
}