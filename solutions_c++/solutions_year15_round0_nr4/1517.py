#include <fstream>
#include <algorithm>
using namespace std;

std::ifstream in("data.in");
std::ofstream out("data.out");


int main() {
    int t;
    int x, r, c;

    in >> t;
    for (int i = 1; i <= t; ++i) {
        in >> x >> r >> c;
        bool result = true;
        if ((r * c) % x != 0) result = false;
        if (x > max(r, c)) result = false;
        if ((x + 1) / 2 > min(r, c)) result = false;

        if (x == 4 && min(r, c) == 2) result = false;

        out << "Case #" << i << ": ";
        out << ((result) ? "GABRIEL\n" : "RICHARD\n");
    }

    return 0;
}
