#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;

int T, A, B, K;
long long R;


int main(){

   ifstream in("Case B.in");
   ofstream out("Solution B.out");

   in >> T;

   for (int t=1; t <= T; t++){
      in >> A >> B >> K;
      R = 0;

      for (int a=0; a < A; a++){
         for (int b=0; b < B; b++){
            int num = (a & b);
            if (num < K && num >= 0)
               R++;

            //cout << a <<" " <<b<<endl;

         }
         //cout << endl;system("PAUSE");
      }

      out << "Case #" << t << ": " << R << endl;


   }

   in.close();
   out.close();

return 0;
}//FIN
