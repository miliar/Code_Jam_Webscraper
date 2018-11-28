#include <iostream>
#include <fstream>
using namespace std;

ifstream input;
ofstream output;

int main() {
    input.open("A-large.in");
    output.open("output.txt");
    int n;
    input >> n;
    for (int i=0; i<n; i++) {
        int maxS;
        string aud;
        input >> maxS >> aud;

        int cur_level = 0;
        int minAdd = 0;
        for (int k=0; k<aud.length(); k++) {
            if (k <= cur_level) {
                cur_level += aud[k]-'0';
            } else if (aud[k]-'0' > 0 && k > cur_level) {
                minAdd += k - cur_level;
                cur_level = k + (aud[k] - '0');
            }
        }
        output << "Case #" << i+1 << ": " << minAdd << "\n";

    }
    input.close();
    output.close();

    return 0;
}
