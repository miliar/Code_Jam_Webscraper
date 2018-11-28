#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int n;
    in >> n;
    for (int i = 0; i < n; ++i) {
        int t;
        in >> t;
        if (t == 0)
            out << "case #" << i + 1 << ": INSOMNIA\n";
        else {
            vector<bool> u(10, false);
            int j = 1;
            while (true) {
                long long t2 = (long long)t * j;
                while (t2) {
                    u[t2 % 10] = true;
                    t2 /= 10;
                }
                int c = 0;
                for (int i = 0; i < 10; ++i) {
                    c += u[i];
                }
                if (c == 10) {
                    out << "case #" << i + 1 << ": " << (long long)t * j << '\n';
                    break;
                }
                ++j;
            }
        }
    }
}