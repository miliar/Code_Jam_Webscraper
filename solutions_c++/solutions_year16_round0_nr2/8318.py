#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream in("B-large.in");
    ofstream out("B-large.out");

    uint32_t num_cases;
    in >> num_cases;

    string newline = "", s = "";

    for (int i = 0; i < num_cases; ++i) {
        in >> s;
        replace(s.begin(), s.end(), '+', '1');
        replace(s.begin(), s.end(), '-', '0');
        bitset<100> bits(s);
        int count = 0;

        for (int j = 0; j < s.length(); ++j) {
            if (bits[j] == 0) {
                count++;
                for (int k = s.length() - 1; k >= j; --k) {
                    bits.flip(k);
                }
            }
        }

        out << newline << "Case #" << i + 1 << ": " << count;
        newline = "\n";
    }

    return 0;
}