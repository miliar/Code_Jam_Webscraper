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

uint32_t minT  = 1000;

void distribute(vector<int> array, int cur){
   int minD = 1000, maxD=0, ithMax=0, ithMin=0, ithEmpty=-1;
   for (int i=0; i<array.size(); i++){
      int d = array[i];
      if (d==0){
         ithEmpty = i;
         continue;
      }
      if (d<minD){
         minD = d;
         ithMin = i;
      }
      if (d>maxD){
         maxD = d;
         ithMax = i;
      }
   }
   //cout << cur << "--->";
   //for (int i=0; i<array.size(); i++)
   //   cout << array[i] << " ";
   //cout << endl;
   if (cur>=minT) return;
   //cout << minT << " " << cur << " " << maxD << " " << minD << endl;
   if (cur+maxD<minT) minT = cur+maxD;
   //cout << "--> " << minT << " " << cur << " " << maxD << " " << minD << endl;
   if (maxD<=3)
      return;

   int diff = maxD-minD;
   if (diff>1){
      for (int j=2; j<=diff/2; j++){
         array[ithMax] = maxD-j;
         array[ithMin] = minD+j;
         distribute(array,cur+1);
         array[ithMax] = maxD;
         array[ithMin] = minD;
      }
   }

   for (int j=2; j<=maxD/2; j++){
      if (ithEmpty<0) array.push_back(j);
      else array[ithEmpty] = j;
      array[ithMax] = maxD-j;
      distribute(array,cur+1);
      if (ithEmpty<0) array.pop_back();
      else array[ithEmpty] = 0;
      array[ithMax] = maxD;
   }

   for (int i=0; i<array.size(); i++){
      if (array[i]>0)
         array[i]--;
   }
   distribute(array,cur+1);
}

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }

   ofstream ofile("B.out");
   int T, D, S, p;
   ifile >> T;
   for ( int i = 0 ; i < T ; ++i ){
      minT = 1000;
      vector<int> array;
      ifile >> D;
      for ( int j=0; j<D; j++){
         int di;
         ifile >> di;
         array.push_back(di);
      }
      distribute(array,0);
      ofile << "Case #" << i+1 << ": " << minT << endl;
      cout << "Case #" << i+1 << ": " << minT << endl;
   }

   ofile.close();
   ifile.close();
   return 0;
}

