#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <utility>
#include <vector>
using namespace std;





int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        // input
        int n, x; 
        cin >> n >> x;
        std::vector<int> cap(n);
        for (size_t i = 0; i < n; ++i) {
            cin >> cap[i];
        }

        int count = 0;
        int front_index = 0;
        int end_index = cap.size() - 1;
        std::sort(cap.begin(), cap.end());
        while(front_index <= end_index) {
            if (cap[end_index] + cap[front_index] <= x) {
                --end_index;
                ++front_index;
                ++count;
            } else {
                --end_index;
                ++count;
            }
        }


        cout << "Case #" << t << ": " << count << endl;
    }


    return 0;
}