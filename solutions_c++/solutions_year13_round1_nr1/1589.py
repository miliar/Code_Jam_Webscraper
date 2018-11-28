#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-small-attempt0.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    ofstream fout;
    fout.open("A-small-attempt0.out");

    int num_cases;
    fin >> num_cases;

    int r, t;

    for (int i=0;i<num_cases;++i)
    {
        fout << "Case #" << i+1 << ": ";
        fin >> r >> t;

        long area = r;
        int total_ring = 0;
        int a = 1;
        while (t > 0)
        {
            long next_area = (r+a)*(r+a);
            long prev_area = (r+a-1)*(r+a-1);
            long area_tofill = next_area - prev_area;
            if (area_tofill > t)
                break;
            else
            {
                total_ring++;
                t -= area_tofill;
            }
            a += 2;
        }
        fout << total_ring;
        fout << endl;
    }

    return 0;
}
