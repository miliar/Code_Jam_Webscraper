#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("data.out");

    int t;
    fin >> t;

    for (int i = 0; i < t; ++i)
    {
        double c,f,x;

        fin >> c >> f >> x;

        double spentTime = 0.0;
        double currentPerSecond = 2.0;
        double currentCookies = 0.0;

        while (currentCookies < x)
        {
            if ((((c - currentCookies) / currentPerSecond) + (x / (currentPerSecond + f))) < ((x - currentCookies) / currentPerSecond))
            {

                spentTime += (c - currentCookies) / currentPerSecond;
                //cout << spentTime << endl;
                //cout << currentPerSecond << endl << endl;
                currentCookies = 0.0;
                currentPerSecond += f;
            }
            else
            {
                spentTime += (x - currentCookies) / currentPerSecond;
                currentCookies = x;
            }
        }

        fout << "Case #" << i + 1 << ": " << setprecision(7) << fixed << spentTime << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
