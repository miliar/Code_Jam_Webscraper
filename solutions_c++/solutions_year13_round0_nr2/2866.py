#include <iostream>
#include <vector>
#include <algorithm>

bool possible(std::vector<std::vector<unsigned short>> const &pattern) {

    std::vector<unsigned short> row_max, col_max;
    row_max.resize(pattern.size());
    col_max.resize(pattern[0].size());

    for (size_t row = 0; row < pattern.size(); ++row)
        row_max[row] = *std::max_element(pattern[row].begin(), pattern[row].end());

    for (size_t col = 0; col < pattern[0].size(); ++col) {
        for (size_t row = 0; row < pattern.size(); ++row)
            col_max[col] = col_max[col] > pattern[row][col] ? col_max[col] : pattern[row][col];
    }

    for (size_t row = 0; row < pattern.size(); ++row)
        for (size_t col = 0; col < pattern[0].size(); ++col)
            if (pattern[row][col] < row_max[row] && pattern[row][col] < col_max[col])
                return false;

    return true;
}

int main() {

    size_t T;
    std::cin >> T;

    for (size_t test = 0; test < T; ++test) {

        // read sizes
        size_t N, M;
        std::cin >> N >> M;

        std::vector<std::vector<unsigned short>> pattern;
        pattern.resize(N);

        // read pattern
        for (size_t nidx = 0; nidx < N; ++nidx) {
            pattern[nidx].resize(M);
            for (size_t midx = 0; midx < M; ++midx)
                std::cin >> pattern[nidx][midx];
        }

        std::cout << "Case #" << test + 1 << ": " << 
                    (possible(pattern) ? "YES" : "NO") << '\n';
    }
}
