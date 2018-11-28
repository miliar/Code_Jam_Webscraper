#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int t;
double c, f, x;
int main()
{
    ifstream in("in.in");
    ofstream out("out.out");
    out.setf(ios::fixed, ios::floatfield);
    out.setf(ios::showpoint);
    int test = 0;
    in >> t;
    while(test < t)
    {
        in >> c >> f >> x;
        double sum1 = 0;
        double sum2 = 0;
        sum2 = x / 2.0;
        double ma = sum2;
        double rate = 2.0;
        for(int i = 1; ; i++)
        {
            sum1 += c / rate;
            rate += f;
            sum2 = x / rate;
            double sum = sum1 + sum2;
            if(sum >= ma)
                break;
            ma = sum;
        }
        out << "Case #" << test + 1 << ": ";
        out << setprecision(7) << ma << endl;
        test++;
    }
}
