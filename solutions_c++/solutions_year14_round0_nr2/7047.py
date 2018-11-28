//Google code jam 2014 Magic Trick

#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <set>

using namespace std;

int TEST_CASES;
double C,F,X,A,tempo;

int main()
{
    cin >> TEST_CASES;
    for (int c = 0; c < TEST_CASES; c++)
    {
		tempo = A = 0;
		cin >> C >> F >> X;
		while ( X/(2+A) > C/(2+A) + X/(2+A+F))
		{
            //cout << tempo << endl;
            tempo+=C/(2+A);
            A+=F;
        }
        tempo += X/(2+A);
        cout << "Case #" << c+1  << ": ";
        cout << fixed << setprecision(7) << tempo << endl;
    }
    return 0;
}
