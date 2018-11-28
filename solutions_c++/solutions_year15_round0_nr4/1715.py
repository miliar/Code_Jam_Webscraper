#include <cassert>
#include <cmath>
#include <iostream>

enum Winner { GABRIEL, RICHARD };

template <typename T>
T max(T a, T b) { return (a > b) ? a : b; }

template <typename T>
T min(T a, T b) { return (a > b) ? b : a; }

Winner solve(int x, int r, int c) {
    const int area = r * c;
    auto bigger = max(r, c);
    if (x > bigger)
        return RICHARD;
    if (area%x != 0) 
        return RICHARD;
    const int squareSize = sqrt(x);
    if (r < squareSize || c < squareSize)
        return RICHARD;
    if (x >= 7)
        return RICHARD;
    auto smaller = min(r,c);
    if ((2* (smaller+1) - 1) <= x)
        return RICHARD;
    if ((2 * smaller) <= x && (x > 2))
        return RICHARD;

    return GABRIEL;
}

void test() {
    assert(solve(2, 2, 2) == GABRIEL);
    assert(solve(2, 1, 3) == RICHARD);
    assert(solve(4, 4, 1) == RICHARD);
    assert(solve(3, 2, 3) == GABRIEL);
    assert(solve(3, 1, 2) == RICHARD);
    assert(solve(4, 2, 2) == RICHARD);
    assert(solve(3, 3, 1) == RICHARD);
    assert(solve(4, 4, 2) == RICHARD);
    assert(solve(2, 1, 2) == GABRIEL);
}

int main() {
    test();

    int T;
    std::cin >> T;
    for (int i = 0; i != T; ++i) {
        int x, r, c;
        std::cin >> x >> r >> c;
        std::cerr << x << " " << r << " " << c << std::endl;
        std::cout << "Case #" << (i+1) << ": " << (solve(x, r, c) == RICHARD ? "RICHARD" : "GABRIEL") << std::endl;
    }
}
