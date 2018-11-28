#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<std::vector<unsigned>> Pattern;

std::vector<Pattern> readPatterns(std::istream& in)
{
    size_t T;
    in >> T;
    std::vector<Pattern> ps;
    ps.reserve(T);
    for (size_t t = 0; t < T; ++t) {
        size_t N, M;
        in >> N >> M;
        Pattern p(N, std::vector<unsigned>(M, 0));
        for (size_t i = 0; i < N; ++i) {
            for (size_t j = 0; j < M; ++j) {
                size_t v;
                in >> v;
                p[i][j] = v;
            }    
        }
        ps.push_back(std::move(p));
    }
    return ps;     
}

unsigned columnMax(const Pattern& p, size_t col)
{
    unsigned m = 0;
    for (size_t i = 0; i < p.size(); ++i)
        m = std::max(m, p[i][col]);
    return m;
}

unsigned rowMax(const Pattern& p, size_t row)
{
    return *std::max_element(p[row].begin(), p[row].end());
}

bool check(const Pattern& p)
{
    std::vector<unsigned> rowMaxs(p.size());
    for (size_t row = 0; row < p.size(); ++row)
        rowMaxs[row] = rowMax(p, row);

    std::vector<unsigned> colMaxs(p.front().size());
    for (size_t col = 0; col < p.front().size(); ++col)
        colMaxs[col] = columnMax(p, col);
 
    for (size_t row = 0; row < p.size(); ++row) {
        for (size_t col = 0; col < p[row].size(); ++col) {
            if (p[row][col] < std::min(rowMaxs[row], colMaxs[col])) {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    auto patterns = readPatterns(std::cin);
    for (size_t i = 0; i < patterns.size(); ++i)
        std::cout << "Case #" << (i + 1) << ": " << (check(patterns[i]) ? "YES" : "NO") << std::endl;
    return 0;
}


