#include <fstream>

using namespace std;

int test, tests, p1, p2, i, j, k, val, a[10][10], b[10][10];

int main()
{
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi >> tests;
    for(test = 1; test <= tests; test++)
    {
        fi >> p1;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                fi >> a[i][j];

        fi >> p2;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                fi >> b[i][j];

        k = 0;
        for(i = 0, p1--, p2--; i < 4; i++)
        {
            for(j = 0; j < 4; j++)
                if(a[p1][i] == b[p2][j]) k++, val = a[p1][i];
        }
        fo << "Case #" << test << ": ";
        if(k == 0) fo << "Volunteer cheated!\n";
        else if(k == 1) fo << val << "\n";
        else fo << "Bad magician!\n";
    }
    return 0;
}
