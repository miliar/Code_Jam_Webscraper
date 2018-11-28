#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin("cookies.in");
    ofstream fout("cookies.out");
    int cases;
    double sum, compsum, comprate, nexttime, c, f, x, rate = 2.00000;
    fin >> cases;
    for(int i=0;i<cases;i++)
    {
        sum=0;
        rate = 2;
        fin >> c >> f >> x;
        comprate=rate+f;
        nexttime = x/rate;
        compsum = sum + c/rate + x/comprate;
        while(compsum<nexttime)
        {
            sum+=c/rate;
            rate+=f;
            nexttime = sum+x/rate;
            comprate = rate+f;
            compsum=sum+c/rate+x/(comprate);
        }
        sum+=x/rate;
        fout << "Case #" << i+1 << ": " << std::fixed << setprecision(7) << sum << endl;
        //cout << "Case #" << i+1 << ": " << std::fixed << setprecision(7) << sum << endl;
    }
    return 0;
}
