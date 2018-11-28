#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <utility>


using namespace std;



int main() {

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int a, b, k;
        cin >> a >> b >> k;

        int count = 0;
        for (int i = 0; i < a; ++i) {
            for (int j = 0; j < b; ++j) {
                int z = i&j;
                if (z < k) {
                    ++count;
                }
            }
        }
        
        cout << "Case #"<< t + 1 << ": "<< count << endl;
    }

    

    return 0;
}