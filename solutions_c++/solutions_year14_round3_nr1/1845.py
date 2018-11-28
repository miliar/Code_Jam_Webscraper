
#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cmath>
#include <sstream>
using namespace std;


int main()
{
    string filename = "A-small-attempt0";
    ifstream infile((filename+".in").c_str());
    ofstream outfile((filename+".out").c_str());

    int T;
    infile >> T;

    long long P;
    long long Q;

    for(int t=0; t<T; t++)
    {
        string s;
        infile >> s;

        string p = s.substr(0,s.find_first_of('/'));
        string q = s.substr(s.find_first_of('/')+1,s.size());

        istringstream sp(p);
        sp >> P;
        istringstream sq(q);
        sq >> Q;
        double x = log2((double)Q/(double)P);

        long long xl = (long long)x;

        if((double)xl != x)
            xl++;

        cout << x << " " << xl << endl;
        if(P*pow(2,xl)==Q)
            outfile << "Case #" << t+1 << ": " << xl << endl;
        else
        {
            double den = log2(Q);
            long long denl = (long long)den;

            if(pow(2, denl) == Q)
                outfile << "Case #" << t+1 << ": " << xl << endl;
            else
                outfile << "Case #" << t+1 << ": " << "impossible" << endl;
        }
    }

    return 0;
}
