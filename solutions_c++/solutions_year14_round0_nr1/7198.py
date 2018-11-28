#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int a[4][4], b[4][4], n, m;
    int t, i, j,p;

    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    fin >> t;
    for(p = 1; p <= t; p++)
    {

        int count = 0, num;
        fin >> n;

        for(i = 0; i < 4; i ++)
            for(j = 0; j < 4; j++)
                fin >> a[i][j];

        fin >> m;

        for(i = 0; i < 4; i ++)
            for(j = 0; j < 4; j++)
                fin >> b[i][j];

        for(j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                if(a[n-1][j] == b[m-1][k])
                {
                    num = a[n-1][j];
                    count++;
                    break;
                }
            }
        }
        fout << "Case #" <<p<<": ";
        if(count == 0) fout << "Volunteer cheated!";
        else if(count == 1) fout << num;
        else fout << "Bad magician!";

        fout << "\n";

    }
    fin.close();
    fout.close();
    return 0;
}
