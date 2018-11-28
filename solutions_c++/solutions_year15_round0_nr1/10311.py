#include <iostream>
#include <fstream>

using namespace std;

ofstream fout;

int main()
{
    ifstream fin;
    fin.open("A-small-attempt0.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    fout.open("A-small-attempt0.out");
    int num_cases;

    fin >> num_cases;
    int num_persons = 0;
    int total_standing = 0;
    int s_max = 0;
    for (int n=0;n<num_cases;++n)
    {
        num_persons = 0;
        total_standing = 0;
        s_max = 0;
        fout << "Case #" << n+1 << ": ";
        fin >> s_max;
        char grid[s_max];
        fin >> grid;
        cout << s_max << endl;
        for (int i=0;i<=s_max;++i)
        {
            int temp = grid[i] - '0';
            if (temp != 0 && total_standing < i)
            {
                num_persons += (i-total_standing);
                total_standing += num_persons;
            }
            total_standing += temp;

        }
        fout << num_persons;
        fout << endl;
    }
    if (fin)
        fin.close();
    if (fout)
        fout.close();
    return  0;
}
