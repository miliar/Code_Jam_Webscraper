#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

double farmTime(int maxFarms, double C, double F, double X)
{
    double timePassed = 0;
    double cps = 2;
    for (int farms = 0; farms < maxFarms; farms++)
    {
        timePassed += C/cps;
        cps += F;
    }
    return X / cps + timePassed;
}

int main()
{
    std::cin.setf( std::ios::fixed, std:: ios::floatfield );
    cin >> setprecision(7);



    ifstream input ("B-large.in");
    if (!input.is_open()) cout << "Failure";
    ofstream output ("output2.txt");
    if (!output.is_open()) cout << "Output Failure";

    //std::ofstream.setf( std::ios::fixed, std:: ios::floatfield );
    output << setprecision(7);
    output << fixed;

    int T;
    input >> T;
    double C [T];
    double F [T];
    double X [T];

    for (int t = 0; t < T; t++)
    {
        //cout << t << endl;
        input >> C[t] >>  F[t] >> X[t];
        //cout << C[t] << "  "<<  F[t] << " " << X[t] << endl;
    }

    for (int t = 0; t < T; t++)
    {
        double cps = 2;
        int maxFarms = 0;

        double fastestTime = farmTime(maxFarms, C[t], F[t], X[t]);
        maxFarms++;
        double result = farmTime(maxFarms, C[t], F[t], X[t]);
        while (true)
        {
            if (result >= fastestTime) break;
            fastestTime = result;
            maxFarms++;
            result = farmTime(maxFarms, C[t], F[t], X[t]);
        }

        output << "Case #" << t+1 << ": "  << fastestTime;
        if (t < T-1) output << endl;
    }
    return 0;
}

