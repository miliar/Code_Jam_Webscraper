#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

int T;
fstream fin,fout;
int a[11][11];
int b[11][11];
int l[11],r[11];
int n,m;

bool check1(int k, int xx)
{
    for (int i = 0; i < m; i++)
        if (a[k][i] != xx && b[k][i]) return false;
    return true;
}

bool check2(int k, int xx)
{
    for (int i = 0; i < n; i++)
        if (a[i][k] != xx && b[i][k]) return false;
    return true;
}

bool xxx()
{
    for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
        if (b[i][j]) return true;
    return false;
}

int main()
{
    fin.open("B-small-attempt0 (1).in",ios::in);
    fout.open("b.txt",ios::out);
    fin >> T;
    for (int k = 0; k < T; k++)
    {
        fin >> n >> m;
        cout << k;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            {
                 fin >> a[i][j];
                 b[i][j] = 1;
                 l[i] = 1;
                 r[j] = 1;
            }
        bool find = true;
        while (xxx())
        {
            find = false;
            int min = 101;

            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    if (a[i][j] < min && b[i][j]) min = a[i][j];
            //cout << min << endl;
            for (int i = 0; i < n; i++)
                if (l[i] && check1(i,min)){
                    for (int j = 0; j < m; j++) b[i][j] = 0;
                    find = true;
                    l[i] = 0;
                }
            for (int i = 0; i < m; i++)
                if (r[i] && check2(i,min)) {
                    for (int j = 0; j < n; j++) b[j][i] = 0;
                    find = true;
                    r[i] = 0;
                }
            if (!find) break;
        }
        if (find) fout << "Case #" << k+1 << ": YES" << endl;
        else fout << "Case #" << k+1 << ": NO" << endl;

    }
    fout.close();
    return 0;
}
