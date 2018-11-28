#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>


using namespace std;

int main()
{
    int n_cases;
    double C,F,X;
    double time;

    ifstream in("B-large.in");
    ofstream out("results.txt");

    in >> n_cases;

    for(int i=0;i<n_cases;++i)
    {
        time =0.0;
        in >> C >> F >> X;

        int n = ceil(X/C -2/F - 1);

        int j;

        for(j=0;j<n;++j)
        {
            time += C/(2 + j*F);
        }
        time += X/(2 + j*F);

        out <<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
    return 0;
}
