#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const char CDATA[] = "B-small-attempt0.in";
const char CRES[]  = "output.out";

int t;

int main()
{
    ifstream fin(CDATA);
    ofstream fout(CRES);
    fin >> t;
    for (int i = 0; i < t; ++i)
    {
       int n,m;
       fin >> n >> m;

       vector < vector<int> > lawn(n, vector<int> (m));

       for (int k = 0; k < n; ++k)
         for (int j = 0; j < m; ++j)
            fin >> lawn[k][j];

       bool gali = true;
       for (int k = 0; k < n; ++k)
         for (int j = 0; j < m; ++j)
            if (lawn[k][j] == 1)
            {
               bool row = true;
               bool col = true;

               for (int y = 0; y < n; ++y)
                  if (lawn[y][j] == 2) col = false;
               for (int y = 0; y < m; ++y)
                  if (lawn[k][y] == 2) row = false;

               if (!row && !col) gali = false;
            }
       fout << "Case #" << i+1 << ": ";
       if (gali)
         fout << "YES\n";
       else
         fout << "NO\n";
    }

    fin.close();
    fout.close();
    return 0;
}
