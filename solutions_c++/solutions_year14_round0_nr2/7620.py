#include <iostream>
#include <fstream>
#include <limits>
using namespace std;

long LONG_MAX = std::numeric_limits<long>::max();

/**
 * C - Cookier required to buy factory
 * F - Factory production per sec.
 * X - Required number of cookies to win
 */
double min_time(double C, double F, double X)
{
    long i = 0;
    for (; i < LONG_MAX; i++)
    {
        double first = X / (2 + i * F);
        double next = (C / (2 + i * F) + X / (2 + (i+1) * F));

        if (next >= first) {
            break;
        }
    }

    double min_time = 0;
    for (long j = 0; j < i; j++) {
        min_time += (C / (2 + j * F)); 
    }

    min_time += X / (2 + i * F);

    return min_time;
}

void cookie_clicker(const char* filename)
{
    int max_line = 65536;
    ifstream input(filename);
    int num_tests;
    input >> num_tests;
    input.ignore(max_line, '\n'); 

    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout.precision(7);
    for (int case_num = 1; case_num <= num_tests; case_num++) 
    {
        double C,F,X;
        input >> C; 
        input >> F; 
        input >> X; 
        input.ignore(max_line, '\n'); 
        cout << "Case #" << case_num << ": " << min_time(C, F, X) << endl;
    }
}

int main(int argc, char* argv[]) {
        if ( argc != 2 ) {
                cout<<"usage: "<< argv[0] <<" <filename>\n";
        }

        cookie_clicker(argv[1]);
        return 0;
}
