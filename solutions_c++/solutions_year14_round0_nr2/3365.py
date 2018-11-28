#include <iomanip>
#include <iostream>
#include <fstream>

using namespace std;


int main ()
{
    ofstream cout ("D:\\outBLARGE.txt");
    ifstream cin ("D:\\DOWNLOADS\\B-large.in");
    //ifstream cin ("D:\\in.txt");
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        long double c, f, x, timeX = 0, minTime = 3e+9, curF = 2;
        cin >> c >> f >> x;
        if (x/2.0 < minTime)
            minTime = x/2.0;
//cout << minTime << endl;
        for (int j = 0; j < 200000; ++j)
        {
            timeX += c / curF;
            curF += f;
            if ((x + curF * timeX) / curF < minTime)
            minTime = (x + curF * timeX) / curF;
            //cout << minTime << endl;
        }
        cout << "Case #" << i + 1 << ": "
         << setprecision(8) << fixed << minTime << endl;
    }

}
