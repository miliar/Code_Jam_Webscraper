#include <iostream>
#include <set>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream fin("B-large.in");
ofstream fout ("out.txt");
//int gcd (int a, int b)
//{
//    while (a != 0 && b != 0)
//    {
//        if (a > b)
//        {
//            a %= b;
//        } else
//        {
//            b %= a;
//        }
//    }
//    return (a == 0) ? b : a;
//}
//
//const int INF = (int) 1e9+42;

int main()
{
    int t;
    fin >> t;
    for (int k = 0; k < t; k++)
    {
        double c, f, x;
        fin >> c >> f >> x;
        vector<double> a((int)(2*x/c)+1, 0.0);
        for (int i = 1; i < a.size(); i++)
        {
            a[i] = a[i-1]+c/(2.0+(double)(i-1)*f);
        }
        double min = 100000.0;
        for (int i = 0; i < a.size(); i++)
        {
            if (min > a[i]+x/(2.0+(double)(i*f)))
            {
                min = a[i]+x/(2.0+(double)(i*f));
            }
        }
        fout << "Case #" << k+1 << ": " ;
        fout << setprecision(7) << fixed << min << endl;
    }
    return 0;
}
