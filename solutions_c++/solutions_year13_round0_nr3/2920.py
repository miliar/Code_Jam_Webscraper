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
#include <algorithm>
#include <math.h>

using namespace std;

uint64_t pal[21] = { 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404 };

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }
   ofstream ofile("C.out");
   int T;
   ifile >> T;
   for ( uint32_t i = 0 ; i < T ; ++i ){
      int S, L;
      ifile >> S >> L;
      int count = 0;
      for ( uint32_t j = 0 ; j < 21 ; ++j ){
         if ( pal[j] >= S && pal[j] <= L )
            count++;
      }
      ofile << "Case #" << i+1 << ": " << count << endl;
      cout << "Case #" << i+1 << ": " << count << endl;
   }

   ofile.close();
   ifile.close();
   return 0;
}
