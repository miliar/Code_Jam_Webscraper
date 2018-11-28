#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream inf("B-large.in");
    ofstream outf("output.txt");

    int t; inf >> t;
    for (int tt = 1; tt <= t; tt++) {
        outf << "Case #" << tt << ": ";
        string pancakes; inf >> pancakes;
        string comp = "";
        char prev = pancakes[0];
        comp += prev;
        for (int i = 1; i < pancakes.length(); i++) {
            if (pancakes[i] != pancakes[i - 1]) {
                prev = pancakes[i];
                comp += prev;
            }
        }
        if (comp[comp.length() - 1] == '-') {
            outf << comp.length() << "\n";
        } else {
            outf << comp.length() - 1 << "\n";
        }
    }
}