#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <utility>
#include <iostream>
#include <cstring>
using namespace std;



int main(int p_Argc, char  **p_Argv)
{
      int T, N ;
      vector<int> M;

     fstream input("A-large.in");
//     fstream input("test.txt");
     ofstream output("titi.txt");

     input >> T;

     for (int nCas=0;nCas<T;nCas++)
     {
         input >> N;
         vector<int> M;
         M.reserve(N);

         for (int u=0;u<N;u++){
            int tt;
            input >> tt;
            M.push_back(tt);
         }

         int ans1 = 0;
         int rate =0;
         for (int u=1; u<N;u++){
            if (M[u] < M[u-1])
            {ans1 += M[u-1]-M[u];
             rate = max(rate, M[u-1]-M[u]);}
         }

         rate = abs(rate);
         int ans2 = 0;

         for (int u=0;u<N-1;u++){
            ans2 += min(rate,M[u]);
         }

         output << "Case #" << nCas+1 << ": " << ans1 << " " << ans2 << endl;


     }

     return 0;
}




