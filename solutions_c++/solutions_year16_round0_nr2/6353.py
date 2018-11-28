#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int count;
    in >> count;
    for (int i = 0; i < count; i++) {
        string pancakes;
        int flips = 0;
        bool happy = false;
        bool first = true;
        in >> pancakes;
        for (int j = 0; j < pancakes.length(); j++) {
            if (first) {
                first = false;
                flips++;
                happy = (pancakes[j] == '+');
            } else {
                if ((!happy && (pancakes[j] == '+')) || (happy && (pancakes[j] == '-'))) {
                    flips++;
                    happy = !happy;
                }
            }
        }
        if (happy) {
            flips--;
        }
        out << "Case #" << i + 1 << ": " << flips << endl;
    }

    in.close();
    out.close();
}
