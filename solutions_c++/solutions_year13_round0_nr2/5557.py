#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int a[100][100];

int check_ground(int n, int m)
{
    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
        {
            if (a[i][j] == 2)
                continue;
            else
            {
                int flag = 0;
                for (int k=0;k<m;k++)
                    if (a[i][k] != 1)
                    {
                        flag = 1;
                        break;
                    }
                if (flag == 1)
                {
                    flag = 0;
                    for (int k=0;k<n;++k)
                        if (a[k][j] != 1)
                        {
                            flag = 1;
                        }
                }
                if (flag == 1)
                {
                    return 0;
                }
            }
        }
    }
    return 1;
}

int main()
{
    ifstream fin;
    fin.open("B-small-attempt2.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    ofstream fout;
    fout.open("B-small-attempt2.out");

    int num_cases;
    fin >> num_cases;

    int amount, n_items;

    for (int c=0;c<num_cases;++c)
    {
        fout << "Case #" << c+1 << ": ";

        int n, m;
        fin >> n >> m;

        for (int i=0;i<n;++i)
            for (int j=0;j<m;j++)
                fin >> a[i][j];

        if (check_ground(n, m) == 0)
            fout << "NO";
        else
            fout << "YES";

        fout << endl;
    }

    return 0;
}
