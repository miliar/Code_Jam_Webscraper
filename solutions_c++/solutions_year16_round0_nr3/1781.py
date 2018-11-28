#include <QCoreApplication>

#include <fstream>
#include <array>
#include <cstdint>

const int N = 32;
const int J = 500;

int main(int argc, char *argv[]) {
    std::ifstream in("in.txt");
    std::ofstream out("out.txt");

    int T;
    in >> T;

    std::array<int, N> arr;
    std::fill(arr.begin(), arr.end(), 0);
    arr[N - 1] = 1;
    out << "Case #1:" << std::endl;
    std::int32_t top_bin = (1 << (N / 2 - 1));
    int cnt = 0;
    for (int i = 0; i <= top_bin && cnt < J; ++i, ++ cnt) {
        std::string res(N, '0');
        res[0] = res[res.size() - 1] = '1';
        std::uint32_t temp = i;
        int j = 1;
        while (temp > 0) {
            if (temp % 2) {
                res[2 *j - 1] = '1';
                res[2 * j] = '1';
            }
            temp /= 2;
            ++j;
        }
        out << res << " ";
        for (int j = 3; j < 12; ++j)
            out << j << " ";
        out << std::endl;
    }

    if (cnt < J) {
        out << "Failed to find enough" << std::endl;
    }

    return 0;
}
