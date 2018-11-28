//Joe Snider
//4/14
//
//Codejam 2014 qual prob 4
// pipe input output (cat input.txt | ./a.out > output.txt)

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int score(vector<double> A, vector<double> B) {
   int ret = 0;
   vector<double>::iterator ib;
   sort(B.begin(), B.end());
   for(vector<double>::iterator ia = A.begin(); ia != A.end(); ++ia) {
      //he finds smallest larger than mine and plays (no score)
      //else he dumps smallest (score)
      ib = upper_bound(B.begin(), B.end(), *ia);
      if(ib != B.end()) {
         B.erase(ib);
      } else {
         B.erase(B.begin());
         ++ret;
      }
   }
   
   return ret;
   
}

int dscore(vector<double> A, vector<double> B) {
   int ret = 0;
   vector<double>::iterator maxA = max_element(A.begin(), A.end());
   vector<double>::iterator minB = min_element(B.begin(), B.end());
   vector<double>::iterator minA = min_element(A.begin(), A.end());
   vector<double>::iterator maxB = max_element(B.begin(), B.end());
   while(A.size() > 0) {
      if(*minA > *minB) {
         //take his smallest with my smallest and score
         A.erase(minA);
         B.erase(minB);
         ++ret;
      } else {
         //take his largest with my smallest, no score
         A.erase(minA);
         B.erase(maxB);
      }
      maxA = max_element(A.begin(), A.end());
      minB = min_element(B.begin(), B.end());
      minA = min_element(A.begin(), A.end());
      maxB = max_element(B.begin(), B.end());
   }
   
   return ret;
}

int main() {
   int T, N;
   cin >> T;
   for(int t = 1; t <= T; ++t) {
      cin >> N;
      vector<double> A(N);
      vector<double> B(N);
      for(int i = 0; i < N; ++i) {cin >> A[i];}
      for(int i = 0; i < N; ++i) {cin >> B[i];}
      cout << "Case #" << t << ": " << dscore(A, B) << " " << score(A,B) << "\n" << flush;
      cout << flush;
   }
}

