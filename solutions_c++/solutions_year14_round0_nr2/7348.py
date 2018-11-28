#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");

int main()
{
    int t;
    in >> t;
    out << setprecision(7) << fixed;
    for (int i = 0; i < t; i++) {
        double c, f, x;
        in >> c >> f >> x;
        double now = 2;
        bool fl = true;
        double time = 0;
        while (fl) {
            if (x / now > c / now + x / (now + f)) {
//                cerr << c / now << endl;
                time += c / now;
                now += f;
            }
            else {
                fl = false;
                time += x / now;
//                cerr << x / now << endl;
            }
        }
        out << "Case #" << i + 1 << ": " << time << endl;
    }

    in.close();
    out.close();
    return 0;
}
