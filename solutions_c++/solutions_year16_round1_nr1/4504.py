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

string prep(string s, char c){
   string s2 = s;
   s2.push_back(c);
   s2[0] = c;
   for (int64_t i=1; i<s2.size(); i++)
      s2[i] = s[i-1];
   return s2;
}

string runRec(string s, int64_t i, string r){
   if (s.size()==r.size()) return r;
   if (r.size()==0) return runRec(s,i+1,s.substr(0,1));
   string r1 = r;
   r1.push_back(s[i]);
   string s1 = runRec(s,i+1,r1);
   string s2 = runRec(s,i+1,prep(r,s[i]));
   if (s1<s2) return s2;
   else return s1;
}

string run(string S){
   return runRec(S,0,"");
}

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }

   ofstream ofile("A.out");
   int T;
   string S;
   ifile >> T;
   for ( int i = 0 ; i < T ; ++i ){
      ifile >> S;
      string r = run(S);
      ofile << "Case #" << i+1 << ": " << r << endl;
      cout << "Case #" << i+1 << ": " << r << endl;
   }
   ofile.close();
   ifile.close();
   return 0;
}
