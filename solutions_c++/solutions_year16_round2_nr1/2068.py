#include <iostream>
#include <string>
#include <map>
#include <vector>

int main() {
    int T, i, j, size, cur;
    std::string S;
    std::map<char, int> m;
    std::map<char, int>::iterator it;
    std::cin >> T;
    std::vector<int> num;
    
    num.resize(10);
    for (i = 1; i <= T; ++i) {
        std::cout << "Case #" << i << ": ";
        std::cin >> S;
        size = S.size();
        m.clear();
        for (j = 0; j < size; ++j) {
            cur = m[S[j]];
            m[S[j]] = cur + 1;
        }
        num[6] = m['X'];
        num[0] = m['Z'];
        num[8] = m['G'];
        num[4] = m['U'];
        num[3] = m['H'] - m['G'];
        num[7] = m['S'] - m['X'];
        num[5] = m['V'] - num[7];
        num[9] = m['I'] - num[8] - num[6] - num[5];
        num[2] = m['W'];
        num[1] = m['O'] - num[4] - num[2] - num[0];
        for (j = 0; j < 10; ++j) {
            for (cur = 0; cur < num[j]; ++cur) {
                std::cout << j;
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
