#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

double optimizer(double C, double F, double X)
{
    double time = 0.0;

    double production = 2.0;

    double cookie = 0.0;

    while(cookie < X)
    {
        if (X/production > (C/production + X/(production+F)))
        {
            time += C/production;
            production += F;
        }
        else
        {
            time += X/production;
            cookie = X+1;
        }
    }

    return time;


}

int main ()
{
    ifstream in("B-large.in");
    ofstream out("output.txt");
    int T;
    in >> T;

    vector<double> result(T);

    float C, F, X;

    for (int j=0; j<T; j++)
    {
        in >> C;
        in >> F;
        in >> X;

        result[j] = (10000000*optimizer(C, F, X)+0.5)/10000000;
    }

    out.precision(12);
    for (int j=0; j<T; j++)
    {
        out << "Case #" << j+1 << ": " << result[j] << endl;

    }

}
