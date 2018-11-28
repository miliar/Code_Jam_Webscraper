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

double A[1005], B[1005];
int T, cant;


int main(){

   ifstream in("Case D.in");
   ofstream out("Solution D.out");

   in >> T;

   for (int t=1; t <= T; t++){
      in >> cant;

      for (int i=0; i < cant; i++)
         in >> A[i];
      for (int i=0; i < cant; i++)
         in >> B[i];

      int W = 0, DW = 0;

      sort (A, A + cant);
      sort (B, B + cant);

      int a=0;                                      // a = iterador de A[]
      for (int i=0; a < cant && i < cant; i++){ // i = iterador de B[]
         while (B[i] < A[a] && i < cant)
            i++;
         if (i < cant)
            a++;
      }
      W = cant - a;

      int lo = 0, hi = cant - 1; //inicio y fin de B[]
      for (int i=0; i < cant; i++){
         if (A[i] < B[lo]){ //elimino el mayor de B[]
            hi--;
         }
         else{
            lo++;
            DW++;
         }
      }

      out << "Case #" << t << ": " << DW << " " << W << endl;

   }

   in.close();
   out.close();

return 0;
}//FIN
