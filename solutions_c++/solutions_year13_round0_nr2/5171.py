#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <functional>
using namespace std;

void redirectIO(string fileName)
{
   static ofstream fout ((fileName + ".out").c_str());
   static ifstream fin ((fileName + ".in").c_str());
   cin.rdbuf(fin.rdbuf());
   cout.rdbuf(fout.rdbuf());
}

bool possible(const vector<vector<unsigned long> > & v)
{
   unsigned N = v.size();
   unsigned M = v[0].size();
   for (unsigned j = 0; j < N; ++j)
   {
      unsigned maxOfRow = *max_element(v[j].begin(), v[j].end());
      for (unsigned k = 0; k < M; ++k)
      {
         if (maxOfRow > v[j][k])
         {
            unsigned maxOfCol = 0;
            for (unsigned p = 0; p < N; ++p)
            {
               if (maxOfCol < v[p][k])
                  maxOfCol = v[p][k];
            }
            if (maxOfCol > v[j][k])
            {
               return false;
            }
         }
      }
   }
   return true;
}

int main()
{
   redirectIO("test");

   unsigned long T, N, M;
   cin>> T;
   vector<bool> resVect (T, false);

   for (unsigned i = 0; i < T; ++i)
   {
      cin>> N>> M;
      vector<vector<unsigned long> > tmp(N, vector<unsigned long>(M));
      for (unsigned j = 0; j < N; ++j)
      {
         for (unsigned k = 0; k < M; ++k)
         {
            cin>> tmp[j][k];
         }
      }
      resVect[i] = possible(tmp);
   }

   for (unsigned i = 0; i < T; ++i)
   {
      cout << "Case #"<<i+1<<": "<<(resVect[i]?"YES":"NO")<<endl;
   }
 
   return 0;
}