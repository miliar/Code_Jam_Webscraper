#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> strs {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int order [] = {0, 2, 6, 7, 4, 5, 3, 1, 8, 9};
char unique_chr [] = {'Z', 'W', 'X', 'S', 'U', 'V', 'R', 'O', 'G', 'E'};

int main() {
    int T, n_case = 1;
    string s;
    std::cin >> T;
    vector<int> v (200, 0), res (10, 0);
    while (T--) {
        std::cin >> s;
        std::fill (v.begin(), v.end(), 0);
        std::fill (res.begin(), res.end(), 0);
        for (auto c : s)
            v[c]++;
        for (int i = 0; i < 10; i++) {
            int n = order[i];
            char c = unique_chr[i];
            while (v[c]) {
                res[n]++;
                for (auto ch : strs[n])
                    v[ch]--;
            }
        }
        std::cout << "Case #" << n_case++ << ": ";
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < res[i]; j++)
               std::cout << i; 
        }
        std::cout << std::endl;
    }

    return 0;
}
