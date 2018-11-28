#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

/* Declarations. */
/* ------------- */
void count_sheep (int n, int iter);

int main (int argc, char *argv[])
{
    char *filename = argv[1];

    string line;

    ifstream infile (filename);
    if (infile.is_open()) {
        for (int i = 0; getline(infile, line); i++) {
            // Skip the # of test cases.
            if (i == 0) continue;

            int n = atoi(line.c_str());

            // Only an input of 0 would result in INSOMNIA.
            if (n == 0) cout << "Case #" << i << ": INSOMNIA" << endl;
            else count_sheep(n, i);
        }
    }
}

void count_sheep (int n, int iter)
{
    int i = 0;

    // bitmap: 0000000000
    unsigned seen = 0;

    while (true) {
        int prod = n * i;

        while (prod > 0) {
            int digit = prod % 10;

            seen |= (1 << digit);

            prod = prod / 10;
        }

        // Have we seen all 10 digits?
        if (seen == 0b1111111111) break;

        i++;
    }

    cout << "Case #" << iter << ": " << n * i << endl;
}
