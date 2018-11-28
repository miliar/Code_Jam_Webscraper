#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin ("solve.in");
    int N;
    fin >> N;

    vector<double> results;
    for(int i = 0; i < N; i++)
    {
        double cost, extra, goal, rate = 2.0;
        fin >> cost >> extra >> goal;
    
        double cookies = 0.0;
        double time = 0.0;
        while(cookies < goal)
        {
            double nextTimeIfNoFactory, nextTimeIfBuyFactory;
            nextTimeIfNoFactory = time + (goal - cookies) / rate;
            nextTimeIfBuyFactory = time + (cost - cookies) / rate + goal / (rate + extra);
            if(nextTimeIfNoFactory <= nextTimeIfBuyFactory)
            {
                results.push_back(nextTimeIfNoFactory);
                break;
            }

            else 
            {
                time = time + (cost - cookies) / rate;
                cookies = 0.0;
                rate += extra;
            }
        }
    }
    fin.close();

    ofstream fout ("solve.out");
    fout << setprecision(100);
    for(int i = 0; i < results.size(); i++)
    {
        fout << "case #" << (i + 1) << ": " << results[i] << "\n";
    }
    fout.close();
    return 0;
}
