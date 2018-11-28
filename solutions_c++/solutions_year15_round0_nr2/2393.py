#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

std::ifstream in("data.in");
std::ofstream out("data.out");

int main() {
    int t, d;
    vector <int> p(2048);

    in >> t;
    for (int i = 1; i <= t; ++i) {
        in >> d;
        for (int j = 1; j <= d; ++j)
            in >> p[j];
        int result = *max_element(p.begin() + 1, p.begin() + d + 1);
        for (int max_elem = 2; max_elem < result; ++max_elem) {
            int temp = max_elem;
            for (int j = 1; j <= d; ++j)
                temp += (p[j] - 1) / max_elem;
            result = min(result, temp);
        }
        out << "Case #" << i << ": " << result << '\n';
    }

    return 0;
}
