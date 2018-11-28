#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream in("small.in");
    ofstream out("out.txt");
    int T;
    in >> T;
    for (int h = 0; h < T; ++h) {
        int n;
        string shyness;
        in >> n >> shyness;
        long cursum = 0;
        long add = 0;
        for (int i = 0; i < shyness.size(); ++i) {
            if (cursum < i) {
                add += i - cursum;
                cursum = i;
            }
            cursum += shyness[i] - '0';
        }
        out << "Case #" << h + 1 << ": ";
        out << add;
        out << endl;
    }
    return 0;
}
