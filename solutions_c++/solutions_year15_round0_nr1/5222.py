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
   ifile >> N;
   for ( int i = 0 ; i < N ; ++i ){
      string str; 
      ifile >> T >> str;
      uint32_t cur = int(str[0])-int('0');
      uint32_t added = 0;
      for ( int j=1; j<str.length(); j++){
         char c = str[j];
         int num = int(c)-int('0');
         if (num>0){
            if (cur<j) { added += j-cur; cur += (j-cur)+num; }
            else cur += num;
         }
      }
      ofile << "Case #" << i+1 << " " << added << endl;
      cout << "Case #" << i+1 << " " << added << endl;
   }

   ofile.close();
   ifile.close();
   return 0;
}
