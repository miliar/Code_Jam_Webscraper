#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>


std::string solution(int x, int r, int c) {
    if (r * c % x != 0) {
        return "RICHARD";
    }
    
    if (x == 1) {
        return "GABRIEL";
    }

    if (x == 2) {
        return "GABRIEL";
    }

    if (x == 3) {
        if (r <= 1 || c <= 1) {
            return "RICHARD";
        } else
        return "GABRIEL";
    }

    if (x == 4) {
        if (r <= 2 || c <= 2) {
            return "RICHARD";
        } else 
        return "GABRIEL";
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    std::cin >> t;
    for (size_t i = 0; i < t; ++i) {
        int x, r, c;
        std::cin >> x >> r >> c;

        std::cout << "Case #" << i + 1 << ": " << solution(x, r, c) << '\n';
    }
}
