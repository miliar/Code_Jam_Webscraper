//Joe Snider
//5/14
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

class CSort {
public:
   bool operator()(const vector<char>& x, const vector<char>& y) const {
      return lexicographical_compare(x.begin(), x.end(), y.begin(), y.end());
   }
};

//turn into normal form (char, reps)
void norm(string& x, vector<char>& lets, vector<int>& count) {
   char prev = 1;
   lets.push_back(prev);
   count.push_back(1);
   for(int i = 0; i < x.size(); ++i) {
      if(x[i] != prev) {
         //new let
         lets.push_back(x[i]);
         count.push_back(1);
         prev = x[i];
      } else {
         count.back() += 1;
      }
   }
}

unsigned long paircheck(const vector<int>& x, const vector<int>& y) {
   unsigned long ret = 0;
   for(int i = 0; i < x.size(); ++i) {
      ret += abs(x[i]-y[i]);
   }
   return ret;
}

void doit(vector<string> words) {
   unsigned val = 0;
   set<vector<char> > s;
   vector<vector<int> > counts;
   for(int i = 0; i < words.size(); ++i) {
      vector<char> li;
      vector<int> ci;
      norm(words[i], li, ci);
      s.insert(li);
      counts.push_back(ci);
   }
   //fail if more than one s (string can't match)
   if(s.size() > 1) {
      cout << "Fegla Won";
      return;
   }
   
   //N=2
   val = paircheck(counts[0], counts[1]);
   
   cout << val;
}

int main() {
   int T;
   int N;
   cin >> T;
   for(int t = 1; t <= T; ++t) {
      cin >> N;
      vector<string> words(N);
      for(int j = 0; j < N; ++j) {
         cin >> words[j];
      }
      cout << "Case #" << t << ": " << flush;
      doit(words);
      cout << "\n" << flush;
   }
}