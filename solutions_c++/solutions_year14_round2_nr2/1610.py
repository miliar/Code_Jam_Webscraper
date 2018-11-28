#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    int t;
    int a, b, k;
    input >> t;
    for (int i = 0; i < t; i++) {
        input >> a >> b >> k;
        int winner = 0;
        for (int x = 0; x < a; x++) {
            for (int y = 0; y < b; y++) {
                int bit = (x & y);
                if (bit < k) {
                    winner++;
                }
            }
        }
        output << "Case #" << i + 1 << ": " << winner << endl;
    }
    return 0;
}
