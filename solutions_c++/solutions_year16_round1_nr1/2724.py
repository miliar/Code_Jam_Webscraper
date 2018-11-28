#include <iostream>

int main() {
    int T;
    std::cin >> T;
    
    for (int i=1; i<=T; i++) {
        std::string S;
        std::cin >> S;

        std::cout << "Case #" << i << ": ";
        std::string ans;
        for (char c: S) {
            if (ans.length() == 0)
                ans += c;
            else if (c >= ans[0])
                ans = c + ans;
            else
                ans += c;
        }
        std::cout << ans << std::endl;
    }
}
