#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int tests;
    fin >> tests;
    for (int t = 1; t <= tests; t++)
    {
        double c, f, x;
        fin >> c >> f >> x;
        double time = 0;
        double cps = 2;
        while (true)
        {
            double time_to_win = x / cps;
            double time_to_next_factory = c / cps;
            double time_to_win_with_ex = time_to_next_factory + x / (cps + f);
            if (time_to_win_with_ex < time_to_win)
            {
                time += time_to_next_factory;
                cps += f;
            }
            else
            {
                time += time_to_win;
                break;
            }
        }
        fout << "Case #" << t << ": " << fixed << setprecision(7) << time << endl;
    }
    fin.close();
    fout.close();
    return 0;
}