#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;

int K, C, S;
void small() {
    for(int i = 0; i < S; ++i) {
        std::cout << " " << i + 1;
    }
    std::cout << std::endl;
}

int main() {
    int CS;
    std::cin >> CS;
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> K >> C >> S;

        std::cout << "Case #" << cs << ":";
        small();
    }

    return 0;
}
