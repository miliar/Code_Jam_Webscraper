#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector <double> results;
    int T;
    cin>>T;
    for (int t = 0; t < T; t++)
    {
        double c, f, x;
        cin>>c>>f>>x;
        double tot = 0.0, cps = 2.0;
        while (1)
        {
            if ((x/cps) < (c/cps) + (x/(cps + f)))
            {
                tot += x/cps;
                break;
            }
            tot += c/cps;
            cps += f;
        }
        results.push_back(tot);
        //cout.precision(7);
        //cout<<fixed<<tot<<endl;
    }
    cout.precision(7);
    for (int i=0;i<results.size();i++)
        cout<<"Case #"<<i+1<<": "<<fixed<<results[i]<<endl;
    return 0;
}
