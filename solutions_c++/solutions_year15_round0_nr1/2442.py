#include <fstream>
using namespace std;

std::ifstream in("data.in");
std::ofstream out("data.out");

int main() {
    int t;
    int smax;
    char buffer[2048];

    in >> t;
    for (int i = 1; i <= t; ++i) {
        in >> smax >> buffer;
        int result = 0;
        int current = 0;
        for (int j = 0; j <= smax; ++j)
            if (buffer[j] != '0') {
                if (current < j) {
                    result += j - current;
                    current += j - current;
                }
                current += buffer[j] - '0';
            }
        out << "Case #" << i << ": " << result << '\n';
    }

    return 0;
}
