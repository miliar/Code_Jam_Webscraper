#include <QCoreApplication>

#include <fstream>
#include <array>
#include <cstdint>

int main(int argc, char *argv[]) {
    std::ifstream in("in.txt");
    std::ofstream out("out.txt");

    int T;
    in >> T;
    for (int i = 1; i <= T; ++i) {
        int n;
        std::array<bool, 10> arr;
        std::fill(arr.begin(), arr.end(), false);
        in >> n;
        std::uint64_t res = 0;
        if (n != 0) {
            int j = 1;
            while (true) {
                std::uint64_t num = j * n;
                while (num > 0) {
                    arr[num % 10] = true;
                    num /= 10;
                }
                if (std::all_of(arr.begin(), arr.end(), [](bool val) {return val;})) {
                    res = j * n;
                    break;
                }
                ++j;
            }
        }
        out << "Case #" << i << ": ";
        if (res == 0)
            out << "INSOMNIA" << std::endl;
        else
            out << res << std::endl;
    }
    return 0;
}
