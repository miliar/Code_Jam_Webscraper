#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

ifstream fin("data.txt");
ofstream fout("output.txt");

void runonce()
{
    double c, f, x;
    fin >> c >> f >> x;

    double result = DBL_MAX;
    
    for (int n = 0; ; ++n)
    {
        double t = 0;
        for (int i = 1; i <= n; ++i)
        {
            t += c / (2 + (i-1) * f);
        }

        t += x / (2 + n * f);

        if (result > t)
            result = t;
        else
            break;

    }

    fout << fixed << setprecision(7) << result << endl;
}

int main()
{
    int case_count;
    fin >> case_count;

    for (int case_id = 1; case_id <= case_count; ++case_id)
    {
        fout << "Case #" << case_id << ": ";
        runonce();
    }

    return 0;
}