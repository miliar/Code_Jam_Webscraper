#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    int T, smax;
    std::string audience;

    std::cin >> T;

    for (int t = 0; t < T; ++t) {
        std::cin >> smax >> audience;
        int current_stand = 0, ans = 0;
        for (int s = 0; s <= smax; ++s) {
            if (current_stand < s) {
                ans += s - current_stand;
                current_stand = s;
            }
            current_stand += audience[s] - '0';
        }
        std::cout << "Case #" << t + 1 << ": " << ans << std::endl;
    }
    return 0;
}
