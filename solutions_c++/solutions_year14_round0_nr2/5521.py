#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

void main()
{
    int T = 0;

    ifstream in("B-large.in");
    ofstream out("B-large.out");

    in >> T;

    double max = 0., maxSolves = 0.;

    for(int i=0; i<T; ++i)
    {
        double X, F, C, 
            solve = numeric_limits<double>::max(), 
            solve2 = 0., 
            predSolve, 
            tmpSolve, 
            k = 1., 
            approximateSteps;
        vector<double> elements;

        in >> C >> F>> X;

        tmpSolve = X / 2.;
        predSolve = C / 2.;

        elements.push_back(C / 2.);

        approximateSteps=(X*F/C-2)/F + 1;

        while(solve>tmpSolve)
        {
            solve = tmpSolve;
            tmpSolve = predSolve + X/(k*F+2.);
            predSolve += C/(k*F + 2.);

            elements.push_back(C/(k*F + 2.));

            k += 1.;
        }

        k -= 1.;

        for(int j = elements.size()-3; j>=0; j--)
            solve2 += elements[j];

        solve2 += X/((k-1)*F+2.);

        if(maxSolves < abs(solve2-solve))
            maxSolves = abs(solve2-solve);

        if (max < abs(k - approximateSteps))
            max = abs(k - approximateSteps);
        
        
        out << "Case #" << i+1 << ": ";
        out << std::fixed << std::setprecision(7);
        out << solve << endl;
    }

    cout <<  "Step approximation error = " << max << endl << "Solves error = " << maxSolves << endl;
}