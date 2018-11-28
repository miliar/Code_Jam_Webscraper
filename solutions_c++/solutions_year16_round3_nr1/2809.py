#include <cassert>
#include <bitset>
#include <cctype>
#include <fstream>
#include <iostream>
#include <vector>

auto arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main(int argc, char** argv)
{
    if (argc < 3) {
        std::cout << "filename input output\n";
        return EXIT_FAILURE;
    }

    std::ifstream input(argv[1]);
    std::ofstream output(argv[2]);
    int T = 0;
    input >> T;
    std::vector<int> P;
    for (int t = 1; t <= T; ++t) {
        int N;
        input >> N;
        P.resize(N);
        int total = 0;
        for (int n = 0; n < N; ++n) {
            input >> P[n];
            total += P[n];
        }
        int evacuated = 0;
        output << "Case #" << t << ": ";
        std::vector<int> more_than_half;
        while (evacuated < total) {
            more_than_half.clear();
            int sum = 0;
            for (int i = 0; i < N; ++i) {
                sum += P[i];
            }
            double half = sum / 2.0;
            for (int i = 0; i < N; ++i) {
                if (P[i] >= half) {
                    more_than_half.push_back(i);
                }
            }
            if (more_than_half.empty()) {
                for (int i = 0; i < N; ++i) {
                    if (P[i] > 0) {
                        more_than_half.push_back(i);
                        break;
                    }
                }
            }
            for (auto i : more_than_half) {
                --P[i];
                ++evacuated;
                output << arr[i];
            }
            output << " ";
        }
        output << "\n";
    }
}