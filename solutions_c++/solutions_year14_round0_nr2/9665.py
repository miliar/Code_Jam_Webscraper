#include <iomanip>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n;

    for (int i = 0; i < n; i++)
    {
        double c, f, x;
        fin >> c >> f >> x;
        int farms = 0;
        double production = 2.0;
        double total_time = 0.0;
        while (true)
        {
            double curr_time = x / production;
            double proj_time = x / (production + f) + c / production;
            if (curr_time < proj_time)
            {
                total_time += x / production;
                break;
            }
            total_time += c / production;
            farms += 1.0;
            production += f;
        }
        fout << setprecision(8) << "Case #" << i + 1 << ": " << total_time << '\n';
    }
}
