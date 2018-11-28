#include <algorithm>
#include <bitset>
#include <iostream>
#include <vector>

int main() {
    std::freopen("in", "r", stdin);
    std::freopen("out", "w", stdout);
    int tn;
    std::cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {        
        int n;
        std::cin >> n;
        bool found = false;
        long long s = n;
        if (n != 0) {
            char buffer[20];
            std::bitset<10> appeared;
            appeared.reset();            
            for (int i = 1; i <= 1000000; ++i) {
                int digits = std::sprintf(buffer, "%lld", s);
                for (int j = 0; j < digits; ++j) {
                    appeared.set(buffer[j] - '0');
                }
                if (appeared.all()) {
                    found = true;
                    break;
                }
                s += n;
            }
        }
        if (found == 0) {
            std::cout << "Case #" << ti << ": INSOMNIA" << '\n';
        } else {
            std::cout << "Case #" << ti << ": " << s << '\n';
        }
    }
}
