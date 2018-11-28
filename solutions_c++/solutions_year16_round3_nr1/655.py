#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, n_case = 1, N, tmp;
    cin >> T;
    while (T--) {
        std::cout << "Case " << "#" << n_case++ << ":";
        vector<int> v;
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> tmp;
            v.push_back(tmp);
        }

        while (true) {
            int max1 = -1, max2 = -1;
            for (int i = 0; i < v.size(); i++) {
                if (v[i] == 0) continue;
                if (max1 == -1) {
                    max1 = i;
                }
                else if (max2 == -1) {
                    max2 = i;
                    if (v[max2] > v[max1]) std::swap(max1, max2);
                }
                else {
                    if (v[max2] < v[i]) max2 = i;
                    if (v[max2] > v[max1]) std::swap(max1, max2);
                }
            }
            if (N == 2) {
                while (v[max1] != v[max2]) {
                    cout << ' ' << static_cast<char>('A'+max1);
                    v[max1]--;
                }
                while (v[max1] != 0) {
                    cout << ' ' << static_cast<char>('A'+max1) << static_cast<char>('A'+max2);
                    v[max1]--;
                }
                break;
            }
            else {
                if (N == 3 && v[max1] == 1) {
                    cout << ' ' << static_cast<char>('A'+max1);
                    v[max1]--;
                }
                else {
                    cout << ' ' << static_cast<char>('A'+max1) << static_cast<char>('A'+max2);
                    v[max1]--;
                    v[max2]--;
                }
                if (v[max1] == 0) N--;
                if (v[max2] == 0) N--;
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
