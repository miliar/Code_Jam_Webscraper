#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    ifstream fin("B.in");
    ofstream fout("B.out");
    int T;
    double C, F, X;
    fin >> T;
    for (int testnum = 1; testnum <= T; testnum++)
    {
        fin >> C >> F >> X;
        int numfarms = max(0, (int) floor((F*X - 2*C)/(F*C)));
        double ans = X/(2+numfarms*F);
        for (int i = 0; i < numfarms; i++)
            ans += C/(2.0 + i*F);
        
        fout << "Case #" << testnum << ": " << fixed << setprecision(7) << ans << endl;
    }
}