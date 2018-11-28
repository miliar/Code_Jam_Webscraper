#include <iostream>
#include <fstream>
using namespace std;
int T;
int a[4][4];
int b[17];
int c,d,e;
int main() {
   ifstream infs("in.txt");
   ofstream oufs("out.txt");
   infs >> T;
   for (int loop = 1; loop <= T; ++loop) {
      for (int d = 0; d != 17;++d)
         b[d]=0; 
      for (int q = 0; q != 2; ++q) {
         infs >> c;
         for (int d = 0; d != 4; ++d)
            for (int e = 0;e!=4;++e)
               infs >> a[d][e];
         ++b[a[c-1][0]]; ++b[a[c-1][1]]; ++b[a[c-1][2]]; ++b[a[c-1][3]];
      }
      c=0;
      for (int i = 1;i !=17; ++i) if (b[i]==2) {++c; d=i;} 
      if (c==1) oufs << "Case #" << loop << ": "<< d << endl;
      if (c==0) oufs << "Case #" << loop << ": Volunteer cheated!" <<endl;
      if (c > 1) oufs << "Case #" << loop << ": Bad magician!" <<endl;
   }
   return   0;
}