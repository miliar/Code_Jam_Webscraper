//Joe Snider
//4/14
//
//Codejam 2014 qual prob 1
// pipe input output (cat input.txt | ./a.out > output.txt)

#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<int> intersect(const vector<int>& x, const vector<int>& y) {
   set<int> ret;
   for(int i = 0; i < x.size(); ++i) {
      for(int j = 0; j < y.size(); ++j) {
	     if(x[i] == y[j]) {
		    ret.insert(x[i]);
		 }
	  }
   }
   return ret;
}

int main() {
   int T, R1, R2, v;
   vector<int> p(4);
   vector<vector<int> > b1(4,p);
   vector<vector<int> > b2(4,p);
   cin >> T;
   for(int t = 1; t <= T; ++t) {
      cin >> R1;
	   for(int i = 0; i < 4; ++i) {
	      for(int j = 0; j < 4; ++j) {
		      cin >> b1[i][j];
		 }
	  }
      cin >> R2;
	   for(int i = 0; i < 4; ++i) {
	      for(int j = 0; j < 4; ++j) {
		      cin >> b2[i][j];
		 }
	  }
     set<int> isec = intersect(b1[R1-1], b2[R2-1]);
     cout << "Case #" << t << ": ";
     if(isec.size()==0) {
        cout << "Volunteer cheated!\n" << flush;
     } else if (isec.size() > 1) {
        cout << "Bad magician!\n" << flush;
     } else {
        cout << *isec.begin() << "\n" << flush;
     }
   }
}
