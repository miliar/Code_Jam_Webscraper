#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main() {
    ifstream in("A-large.in");
    ofstream out("A-large.out");

    uint32_t num_cases, n, ns;
    string newline = "";
    div_t divs;
    set<uint8_t> seen;

    in >> num_cases;

    for (int i = 0; i < num_cases; ++i) {
        in >> n;
        if (n) {
            ns = n;
            seen.clear();
            do {
                divs.quot = ns;
                do {
                    divs = div(divs.quot, 10);
                    seen.insert(divs.rem);
                } while (divs.quot > 0);
            } while ((seen.size() < 10) && (ns = ns + n));
            out << newline << "Case #" << i + 1 << ": " << ns;
        } else {
            out << newline << "Case #" << i + 1 << ": INSOMNIA";
        }
        newline = "\n";
    }

    return 0;
}