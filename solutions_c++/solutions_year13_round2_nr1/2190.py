#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <map>
#include <stdlib.h>
#include <cstdio>
#include <set>
#include <iterator>
#include <bitset>
#include <algorithm>

using namespace std;

int A, N;
int Nmin;

void play(multiset<int> motes, int nm, int A) {
   //cout << "gh1 " << nm << " " << Nmin << " " << A << " " << "\n";
   //copy(motes.begin(), motes.end(), ostream_iterator<int>(cout, " "));
   //cout << "\n";
   if(motes.size() == 0) {
      Nmin = (nm<Nmin)?nm:Nmin; //extra test
      return;
   } else if (nm > Nmin) {
      //fail
      return;
   } else {
      if(A > *motes.begin()) {
         //eat
         A += *motes.begin();
         motes.erase(motes.begin());
         play(motes, nm, A);
      } else {
         ++nm;
         //pop off the end
         multiset<int> m2 = motes;
         m2.erase(--(m2.end()));
         play(m2, nm, A);
         
         //add the largest edible
         multiset<int> m3 = motes;
         m3.insert(A-1);
         play(m3, nm, A);
      }
   }
}

int main() {
   int T, t;
   cin >> T;
   for(int n = 0; n < T; ++n) {
      cout << "Case #" << n+1 << ": ";
      cin >> A >> N;
      multiset<int> motes;
      for(int i = 0; i < N; ++i) {
         cin >> t;
         motes.insert(t);
      }
      Nmin = motes.size();
      play(motes, 0, A);
      cout << Nmin << "\n";
   }
}

