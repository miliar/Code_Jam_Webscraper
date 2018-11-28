
#include <iostream>
#include <iomanip>

using namespace std;

class problem {
    double c, f, x;
public:
    problem(istream &is) {
        is >> c >> f >> x;
    }

    problem(double c_, double f_, double x_) 
        : c(c_), f(f_), x(x_) {
    }
        

    double solve() {
        if (c >= x) {
            return x / 2.0;
        }

        double base = 0.0;
        double off  = c / 2.0;
        double slope = 2.0;
        double newslope = slope + f;
        int buy = 0;

        while (true) {
//            cerr << "t = " << base << endl;
            if (x / slope > x / newslope + off) {
                // buy
//                cerr << "buy\n";
                base += off;
                off  = c / newslope;
                slope = newslope;
                newslope = slope + f;

                buy++;
            }
            else {

//                 cerr << "bought " << buy << endl;
                // no buy
//                cerr << "no buy\n";
                return base + (x / slope);
            }
        }
    }
};

int main(int argc, char *argv[])
{
    // problem p(500.0, 4.0, 2000.0);
    // cout << p.solve() << endl;

    cout << setprecision(20);

    int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        problem p(cin);
        cout << "Case #" << i << ": " << p.solve() << "\n";
    }

    return 0;
}
