#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

using namespace std;


void solveCase(std::ifstream& in, std::ostream& out) noexcept {
    long long N;
    in >> N;
    uint16_t found = 0b0000000000;
    uint16_t all = 0b1111111111;
    auto last = N;
    int i = 2;
    auto lookForNumbers = [&](long long number) {
        std::string str = std::to_string(number);
        for (int i = 0; i < 10; i++) {
            if (str.find(std::to_string(i)) != std::string::npos) {
                found |= 1 << i;
            }
        }
    };
    lookForNumbers(last);
    while(true) {
        last = N * i++;
        if (last == N) {
            out << "INSOMNIA";
            break;
        }
        lookForNumbers(last);
        if (found == all) {
            out << last;
            break;
        }
    }
}

void solve(std::ifstream& in, std::ostream& out) noexcept {

    int T;
    in >> T;
    int t = 0;
    while (t++ < T) {
        out << "Case #" << t << ": ";
        solveCase(in, out);
        out << std::endl;
        out.flush();
    }
}

int main(int argc, char* argv[]) {
    ifstream in(argv[1]);
    ofstream out = ofstream(argv[2]);
    solve(in, out);
    return 0;
}