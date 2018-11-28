#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <fstream>
#include <cstdint>
#include <queue>
#include <map>
#include <unordered_map>
#include <iostream>

template<typename SolveClass>
class CodejamTests
{
public:
    CodejamTests(const std::string& input, const std::string& output)
    {
        std::ifstream in(input);
        std::ofstream out(output);
        SolveClass obj;

        size_t maxTests = 0;
        in >> maxTests;
        for (size_t test = 1; test <= maxTests; ++test) {
            in >> obj;
            obj.solve();
            out << "Case #" << test << ": " << obj << "\n";
        }
    }
};

class Dijkstra
{
    friend std::istream& operator>>(std::istream& is, Dijkstra& obj);
    friend std::ostream& operator<<(std::ostream& os, const Dijkstra& obj);

    std::string s;
    std::string result;
    std::vector<int> columns;
    std::vector< std::vector<int> > dp;
public:
    void solve()
    {
        const auto N = s.size();
        const int matrix[5][5] = {
            0, 0, 0, 0, 0,
            0, 1, 2, 3, 4,
            0, 2, -1, 4, -3,
            0, 3, -4, -1, 2,
            0, 4, 3, -2, -1
        };

        //columns.clear();
        columns.resize(N);
        std::transform(std::begin(s), std::end(s), std::begin(columns), [](char c) {
            switch (c)
            {
            case 'i': return 2;
            case 'j': return 3;
            case 'k': return 4;
            }
            return 0;
        });
        //dp.clear();
        dp.resize(N);
        std::for_each(std::begin(dp), std::end(dp), [N](std::vector<int>& row){
            row.resize(N);
        });
        for (size_t i = 0; i < N; ++i) {
            dp[i][i] = columns[i];
            for (size_t j = i + 1; j < N; ++j) {
                const auto& row = dp[i][j - 1];
                if (row < 0) {
                    dp[i][j] = -matrix[-row][columns[j]];
                } else {
                    dp[i][j] = matrix[row][columns[j]];
                }
            }
        }

        result = "NO";
        bool isContinue = true;
        for (size_t i = 0; i < N && isContinue; ++i) {
            if (2 != dp[0][i]) {
                continue;
            }
            for (size_t j = i + 1; j < N - 1; ++j) {
                if (3 != dp[i + 1][j]) {
                    continue;
                }
                if (4 == dp[j + 1][N - 1]) {
                    result = "YES";
                    //std::cout << "[0.." << i << "][" << i + 1 << ".." << j << "][" << j + 1 << ".." << N - 1 << "]\n";
                    isContinue = false;
                    break;
                }
            }
        }
    }
};
std::istream& operator>>(std::istream& is, Dijkstra& obj)
{
    size_t L = 0, X = 0;
    std::string str;
    is >> L >> X;
    is >> str;
    obj.s.clear();
    for (size_t i = 0; i < X; ++i) {
        obj.s += str;
    }
    return is;
}
std::ostream& operator<<(std::ostream& os, const Dijkstra& obj)
{
    os << obj.result;
    return os;
}

int
main()
{
    CodejamTests<Dijkstra> testC("C.in", "C.out");
    return 0;
}
