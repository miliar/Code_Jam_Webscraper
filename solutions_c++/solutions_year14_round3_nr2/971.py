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

int T;
string tren[105];
int connected[105];
bool usado[105];
bool letras[30];
int N;
long long R, cant=0;
long long MOD = 1000000007;


void busca_formas(){



   if (cant == N){
      fill(letras, letras + 27, false);

      char actual = tren[connected[0]][0];
      letras[actual - 'a'] = true;

      for (int i=0; i<cant; i++)
         for (int j=0; j < tren [connected[i]].size(); j++){
            if (tren[connected[i]] [j] != actual){ //letra nueva
               actual = tren[connected[i]] [j];
               if (letras[actual - 'a'])
                  return; //no esta adyacente. muere

               letras[actual-'a'] = true;

            }

         }

         /*for (int i=0; i<cant; i++)
         for (int j=0; j < tren [connected[i]].size(); j++)
            cout <<tren[connected[i]] [j];cout << endl;*/


      R++;
      R %= MOD;
   }
   else{

      for (int i=0; i < N; i++){
         //if (cant != 0 && tren[i].first != tren [connected[cant-1] ].second)
            //continue;
         if (usado[i])
            continue;

         connected[cant++] = i;
         usado[i] = true;

         busca_formas();

         usado[i] = false;
         --cant;
      }


   }

}//FIN


int main(){

   ifstream in("Case B.in");
   ofstream out("Solution B.out");

   in >> T;

   for (int t=1; t <= T; t++){
      in >> N;

      for (int i=0; i < N; i++)
         in >> tren[i];

      //for (int i=0; i < N; i++)cout <<tren[i].first<<" "<<tren[i].second<<endl;
      fill(usado, usado + 101, false);
      cant=0; R=0;

      busca_formas();

      out << "Case #" << t << ": " << R << endl;

   }



   in.close();
   out.close();

return 0;
}//FIN
