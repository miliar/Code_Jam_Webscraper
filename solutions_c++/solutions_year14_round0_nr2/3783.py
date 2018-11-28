#include <fstream>
#include <iomanip>

using namespace std;

double timp, x, t, c, f;
int test, tests;
int main()
{
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi >> tests;
    for(test = 1; test <= tests; test++)
    {
        fi >> c >> f >> x;
        for(t = 2, timp = 0; ; t += f)
        {
            if(x/t < (c/t + x/(t+f)))
            {
                timp += x/t;
                break;
            }
            else
                timp += c/t;
        }
        fo << "Case #" << test << ": ";
        fo << setprecision(7) << fixed;
        fo << timp << "\n";
    }
    return 0;
}
