#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ifstream file("a.in");
    int T;
    file >> T;
    for (int x = 0; x < T; x++) {
        int smax;
        file >> smax;

        string audience;
        file >> audience;

        vector<int> xs;
        xs.reserve(audience.size());
        for (int i = 0; i < audience.length(); i++) {
            xs.push_back(audience[i] - '0');
        }

        int n = 0;
        int acc = 0;
        for (int i = 0; i < xs.size(); i++) {
            if (acc < i) {
                xs[i] += i - acc;
                n += i - acc;
            }
            acc += xs[i];
        }

        std::cout << "Case #" << (x + 1) << ": " << n << '\n';
    }
}
