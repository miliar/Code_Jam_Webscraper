#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ofstream fout("output.out");
    ifstream fin("input.in");
    int test, str;
    string a, b;
    fin >> test;

    for(int i = 0; i < test; ++i)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> str;
        fin >> a;
        fin >> b;

        if(a == b)
        {
            fout << 0 << endl;
            continue;
        }

        vector<vector<int> > t(a.size() + 1);
        t[0].resize(b.size() + 1);
        t[0][0] = 0;
        for(int i = 1; i <= a.size(); ++i)
        {
            t[i].resize(b.size() + 1);
            t[i][0] = -1;
        }
        for(int i = 1; i <= b.size(); ++i)
        {
            t[0][i] = -1;
        }
        for(int i = 1; i <= a.size(); ++i)
        {
            for(int j = 1; j <= b.size(); ++j)
            {
                if(a[i-1] == b[j-1])
                {
                    if(t[i-1][j-1] != -1) t[i][j] = t[i-1][j-1];
                    else
                    {
                        t[i][j] = t[i][j-1];
                        if(t[i][j] == -1 && t[i-1][j] != -1) t[i][j] = t[i-1][j];
                        else if(t[i-1][j] != -1 && t[i-1][j] < t[i][j]) t[i][j] = t[i-1][j];
                        if(t[i][j] != -1) t[i][j]++;
                    }
                }
                else
                {
                    t[i][j] = -1;
                }
            }
        }
        if(t[a.size()][b.size()] != -1)
            fout << t[a.size()][b.size()];
        else
            fout << "Fegla Won";
        fout << endl;
    }

    return 0;
}
