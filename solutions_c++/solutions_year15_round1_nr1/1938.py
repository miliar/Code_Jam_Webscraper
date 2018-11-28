 /* Copyright NTU GIEE 2012. All Rights Reserved. */
 /* =====================================================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  04/14/2012 12:42:55 PM CST
 *         Author:  Bo-Han Gary Wu (NTU GIEE), researchgary@gmail.com
 * ===================================================================================== */

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <cassert>
#include <vector>
#include <stdint.h>

using namespace std;

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }

   ofstream ofile("A.out");
   int T, N, S, p;
   ifile >> T;
   for ( int i = 0 ; i < T ; ++i ){
      int32_t n;
      vector<int32_t> array;
      ifile >> N;
      cout << N << endl;
      for (int j=0; j<N; j++){
         ifile >> n;
         array.push_back(n);
      }
      int32_t first = 0;
      int32_t second = 0;
      // first
      int32_t prev = array[0];
      int32_t maxDiff = 0;
      for (int j=1; j<N; j++){
         int32_t cur = array[j];
         int32_t diff = prev-cur;
         if (diff>0) first += diff;
         if (diff>maxDiff) maxDiff = diff;
         prev = cur;
      }
      for (int j=0; j<N-1; j++){
         int32_t cur = array[j];
         if (maxDiff>cur) second += cur;
         else second += maxDiff;
      }

      ofile << "Case #" << i+1 << ": " << first << " " << second << endl;
      cout << "Case #" << i+1 << ": " << first << " " << second << endl;
   }

   ofile.close();
   ifile.close();
   return 0;
}
