#include <iostream>
#include <string>

std::string solve(int x, int r, int c) {
    if (r * c % x != 0 || r < x) {
        return "RICHARD";
    } else {
        if (x == 1) {
            return "GABRIEL";
        } else if (x == 2) {
            return "GABRIEL";
        } else if (x == 3) {
            if (c == 1) return "RICHARD";
            if (c == 2) return "GABRIEL";
            if (c == 3) return "GABRIEL";
            if (r == 4) return "GABRIEL";
        } else if (x == 4) {
            if (c == 1) return "RICHARD";
            if (c == 2) return "RICHARD";
            if (c == 3) return "GABRIEL";
            if (c == 4) return "GABRIEL";
        }
    }
    return "";
}

int main(int argc, char *argv[]) {
    int T, x, r, c;
    std::string ans;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        std::cin >> x >> r >> c;
        if (r < c) {
            std::cout << "Case #" << t + 1 << ": " << solve(x, c, r) << std::endl;;
        } else {
            std::cout << "Case #" << t + 1 << ": " << solve(x, r, c) << std::endl;
        }
    }
    return 0;
}
