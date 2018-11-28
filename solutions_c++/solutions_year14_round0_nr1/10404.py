#include <iostream>
#include <vector>
#include <fstream>

using namespace::std;

int main() {
   fstream ifile, ofile;
   int NumTestCases = 1, i, j, cases;
//   ifile.open("pa.in", ios::in);
   ifile.open("A-small-attempt0.in", ios::in);
   ofile.open("A-small-attempt0.out", ios::out);
   ifile >> NumTestCases;
   for(cases = 1; cases <= NumTestCases; cases++) {
      int ans1, ans2;
      int m1[4][4], m2[4][4];
      vector<int> common;
      ifile >> ans1;
//      cout<< ans1 << "\n";
      for(j = 0; j < 4; j++) {
         ifile >> m1[j][0] >> m1[j][1] >>m1[j][2] >>m1[j][3];
//         cout << m1[j][0] << " " << m1[j][1] << " " <<m1[j][2] << " " <<m1[j][3] << "\n";
      }
      ifile >> ans2;
//      cout<< ans2 << "\n";
      for(j = 0; j < 4; j++) {
         ifile >> m2[j][0] >> m2[j][1] >>m2[j][2] >>m2[j][3];
//         cout << m2[j][0] << " " << m2[j][1] << " " <<m2[j][2] << " " <<m2[j][3] << "\n";
      }

      common.clear();

      for(i = 0; i < 4; i++ ) {
         for(j = 0; j < 4; j++) {
            if(m1[ans1-1][i] == m2[ans2-1][j]) {
	       common.push_back(m1[ans1-1][i]);
	       break;
            }
         }
      }

      if(common.size() == 1) {
	 ofile << "Case #" << cases <<": " << common[0]<<"\n"; 
      }
      else if(common.size() > 1) {
	 ofile << "Case #" << cases <<": Bad magician!"<<"\n"; 
      }
      else {
	 ofile << "Case #" << cases <<": Volunteer cheated!"<<"\n"; 
      }
      common.clear();
      
   }
   ifile.close();
   ofile.close();
   return 0;
}
