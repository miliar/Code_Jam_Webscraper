#include <bits/stdc++.h>
using namespace std;


int main(int narg, char *args[]){

   ifstream in ("in1.in");
   ofstream out ("out1.out");

   int T;
   int Smax;
   string S;
   in >> T;

   for (int t=1; t <= T; t++){
      in >> Smax >> S;
      int R = 0, sum = 0, tam = S.size();

      for (int i = 0; i < tam; i++){
         if (sum >= i){ //Se paran las personitas
            sum += (int)(S[i] - '0');
         }
         else{//Invito amigos
            R += i - sum;
            sum += (int)(S[i] - '0') + (i - sum);
         }

      }

      out << "Case #" << t << ": " << R << endl;

   }

   in.close();
   out.close();

   return 0;
}//end main
