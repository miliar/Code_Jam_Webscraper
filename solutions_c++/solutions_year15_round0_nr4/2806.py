#include <cmath>
#include <iostream>

#include <vector>

/* s_shape */
// typedef struct shape {
//     std::vector<bool> X;
//     int R;
//     int C;
// } s_shape;

/* _n_ominoes */
// static std::vector<s_shape> _1_ominoes(1);
// static std::vector<s_shape> _2_ominoes(1);
// static std::vector<s_shape> _3_ominoes(2);
// static std::vector<s_shape> _4_ominoes(5);


// inline int get(const s_shape &s, int r, int c) {
//     return s.X[r * s.R + s.C];
// }

// inline void set(const s_shape &s, int r, int c, int v) {
//     s.X[r * s.R + s.C] = v;
// }

// void add(s_shape &M, const s_shape &s) {
//     for (int r = 0; r < s.R; ++r) {
//         for (int c = 0; c < s.C; ++c) {
//             set(M, r, c) = get(s, r, c);
//         }
//     }
// }

// bool play(const std::vector<s_shape> &ominoes, const s_shape &s, int R,  int C) {
//     std::vector<bool> X(R * C, false);
//     s_shape M = {X, R, C};
//     for (int r = 0; r < R - s.R; ++r) {
//         for (int c = 0; c < C - s.C; ++c) {
//             ...
//         }
//     }
// }

bool game(int X, int R, int C) {
    if ((R * C) % X) {
        return false;
    }
    int w = std::ceil(double(X) / 2.0);
    if (w > R || w > C) {
        return false;
    }
    // std::vector<s_shape> ominoes;
    switch (X) {
    case 1:
        return true;
        // ominoes = _1_ominoes;
        break;
    case 2:
        return true;
        // ominoes = _2_ominoes;
        break;
    case 3:
        return true;
        // ominoes = _3_ominoes;
        break;
    case 4:
        if (R > 2 && C > 2) {
            return true;
        } else {
            return false;
        }
        // ominoes = _4_ominoes;
        break;
    default:
        return false;
    }
}

int main(int argc, char **argv) {
    /* 1_ominoes */
    // _1_ominoes.push_back({{1}, 1, 1});
    /* 2_ominoes */
    // _2_ominoes.push_back({{1, 1}, 1, 2});
    // _2_ominoes.push_back({{1, 1}, 2, 1});
    /* 3_ominoes */
    // _3_ominoes.push_back({{1, 1, 1}, 1, 3});
    // _3_ominoes.push_back({{1, 1, 1}, 3, 1});
    // _3_ominoes.push_back({{0, 1, 1, 1}, 2, 2});
    // _3_ominoes.push_back({{1, 0, 1, 1}, 2, 2});
    // _3_ominoes.push_back({{1, 1, 0, 1}, 2, 2});
    // _3_ominoes.push_back({{1, 1, 1, 0}, 2, 2});
    /* 4_ominoes */
    // _4_ominoes.push_back({{1, 1, 1, 1}, 2, 2});
    // _4_ominoes.push_back({{1, 1, 1, 1}, 1, 4});
    // _4_ominoes.push_back({{1, 1, 1, 1}, 4, 1});
    // _4_ominoes.push_back({{0, 1, 0, 1, 1, 1}, 2, 3});
    // _4_ominoes.push_back({{0, 1, 1, 0, 1, 1}, 2, 3});
    // _4_ominoes.push_back({{0, 1, 1, 1, 0, 1}, 2, 3});
    // _4_ominoes.push_back({{0, 1, 1, 1, 1, 0}, 2, 3});
    // _4_ominoes.push_back({{1, 0, 0, 1, 1, 1}, 2, 3});
    // _4_ominoes.push_back({{1, 0, 1, 0, 1, 1}, 2, 3});
    // _4_ominoes.push_back({{1, 0, 1, 1, 0, 1}, 2, 3});
    // _4_ominoes.push_back({{1, 0, 1, 1, 1, 0}, 2, 3});
    // _4_ominoes.push_back({{1, 1, 0, 1, 0, 1}, 2, 3});
    // _4_ominoes.push_back({{1, 1, 0, 1, 1, 0}, 2, 3});
    // _4_ominoes.push_back({{1, 1, 1, 0, 0, 1}, 2, 3});
    // _4_ominoes.push_back({{1, 1, 1, 0, 1, 0}, 2, 3});
    // _4_ominoes.push_back({{0, 0, 1, 1, 1, 1}, 3, 2});
    // _4_ominoes.push_back({{0, 1, 0, 1, 1, 1}, 3, 2});
    // _4_ominoes.push_back({{0, 1, 1, 1, 0, 1}, 3, 2});
    // _4_ominoes.push_back({{0, 1, 1, 1, 1, 0}, 3, 2});
    // _4_ominoes.push_back({{1, 0, 0, 1, 1, 1}, 3, 2});
    // _4_ominoes.push_back({{1, 0, 1, 0, 1, 1}, 3, 2});
    // _4_ominoes.push_back({{1, 0, 1, 1, 1, 0}, 3, 2});
    // _4_ominoes.push_back({{1, 1, 0, 0, 1, 1}, 3, 2});
    // _4_ominoes.push_back({{1, 1, 0, 1, 0, 1}, 3, 2});
    // _4_ominoes.push_back({{1, 1, 1, 0, 0, 1}, 3, 2});
    // _4_ominoes.push_back({{1, 1, 1, 0, 1, 0}, 3, 2});
    // _4_ominoes.push_back({{1, 1, 1, 1, 0, 0}, 3, 2});
    /* algorithm */
    int T = 0;
    std::cin >> T;
    for (int x = 0; x < T; ++x) {
        int X = 0, R = 0, C = 0;
        std::cin >> X >> R >> C;
        std::cout << "Case #" << x + 1 << ": ";
        if (game(X, R, C)) {
            std::cout << "GABRIEL";
        } else {
            std::cout << "RICHARD";
        }
        std::cout << std::endl;
    }
    return 0;
}
