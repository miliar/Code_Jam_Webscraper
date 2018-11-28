#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <fstream>
using namespace std;

double C, F, X;
double G, tiempo;
int cookies, T;
double R = 100005;


int main(){

   ifstream in("Case B.in");
   ofstream out("Solution B.out");

   in >> T;

   for (int t=1; t <= T; t++){

      in >> C >> F >> X;

      int N = 0; //cantidad de COOKIES que compraré
      R = 100005;

      for (; N < 100000; N++){
         double suma = 0;

         for (int i=0; i <= N; i++){
            if (i == N){
               suma += X / (2 + i * F);
            }
            else{
               suma += C / (2 + i * F);
            }
         }

         if (suma > R)
            break;
         else
            R = suma;

      }

      out << "Case #" << t << ": " << fixed << setprecision(7) << R << endl;
   }

   in.close();
   out.close();
return 0;
}//FIN
