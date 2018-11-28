#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int main()
{
   int test;
   in >> test;
   for (int t = 1; t <= test; ++t)
   {
      int n, m;
      in >> n >> m;
      vector < vector <int> > a(n, vector <int>(m));
      for (int i = 0; i < n; ++i)
         for (int j = 0; j < m; ++j)
            in >> a[i][j];
      bool f = true;
      for (int i = 0; i < n; ++i)
      {
         int maxim = a[i][0];
         for (int j = 0; j < m; ++j)
            maxim = max(maxim, a[i][j]);
         for (int j = 0; j < m; ++j)
            if (a[i][j] != maxim)
            {
               for (int k = 0; k < n; ++k)
                  if (a[k][j] > a[i][j])
                     f = false;
            }
      }
      out << "Case #" << t << ": " << (f?"YES":"NO") << endl;
   }  

   return 0;
}




