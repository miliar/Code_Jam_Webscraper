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

int T, cant;
string a, b;


int main(){

   ifstream in("Case A.in");
   ofstream out("Solution A.out");

   in >> T;

   for (int t=1; t <= T; t++){
      long long R = 0;
      in >> cant >> a >> b;

      char ant = 'L';

      for (int i=0, j=0; i < a.size() || j < b.size(); i++, j++){
         //system("PAUSE"); cout << a <<"  " << b<< " i=" << i << " j=" << j <<endl;
         if (a[i] == b[j]){
            ant = a[i];

         }
         else if (a[i] == ant){
            b.insert (j-1, 1, ant);
            R++;
         }
         else if (b[j] == ant){
            a.insert(i-1, 1, ant);
            R++;
         }
         else{
            R = -1;
            break;
         }

      }

      if (R == -1)
         out << "Case #" << t << ": Fegla Won" << endl;
      else
         out << "Case #" << t << ": " << R << endl;

   }



   in.close();
   out.close();

return 0;
}//FIN
