#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    if(!in.is_open())
    {
        cerr << "Upss!\n";
        return 1;
    }

    int testCases;
    in >> testCases;

    double C[testCases], F[testCases], X[testCases];
    int cnt = 0;
    while(!in.eof())
    {
        in >> C[cnt] >> F[cnt] >> X[cnt];
        cnt++;
    }

    ofstream out("B-large.out");

    double cookiePerSec = 2.0;
    double totalTime = 0.0;
    double optimumTime = 0.0;
    bool cont = true;

    for(int i = 0; i < testCases; i++)
    {
        optimumTime = X[i] / cookiePerSec;
        totalTime += C[i] / cookiePerSec;
        if(totalTime >= optimumTime)
        {
            out << "Case #" << i + 1 << ": " << std::fixed << optimumTime << endl;
        } else
        {
            cont = true;
            while(cont)
            {
                cookiePerSec += F[i];
                double a = (X[i] / cookiePerSec) + totalTime;
                totalTime += C[i] / cookiePerSec;

                if(a > optimumTime)
                {
                    cont = false;
                    out << "Case #" << i + 1 << ": "  << std::fixed << optimumTime << endl;
                }
                optimumTime = a;
            }
        }
        totalTime = 0;
        cookiePerSec = 2.0;
    }


    return 0;
}

