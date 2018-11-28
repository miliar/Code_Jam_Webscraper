#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;


void solveCase(std::ifstream& in, std::ostream& out) noexcept {
    string str;
    in >> str;
    int moves = 0;

    string::size_type idx;
    while ((idx = str.find_last_of('-')) != string::npos) {
        moves++;
        for (auto i = idx; i != string::npos; i--) {
            str[i] = str[i] == '-' ? '+' : '-';
        }
    }
    out << moves;
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