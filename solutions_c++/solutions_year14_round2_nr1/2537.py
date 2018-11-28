#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <bitset>

using namespace std;

vector<char> getLetters(const string &str, vector<int> &counts) {
   vector<char> letters;
   counts.clear();
   letters.push_back(str[0]);
   int c = 1;
   for(int i = 1; i < str.size(); i++) {
      if(str[i] != str[i-1]){
         letters.push_back(str[i]);
         counts.push_back(c);
         c = 1;
      }
      else
         c++;
   }
   counts.push_back(c);

   return letters;
}


bool same(const vector<char> &v1, const vector<char> &v2) {
   if(v1.size() != v2.size())
      return false;
   for(int i = 0; i < v1.size(); i++)
      if(v1[i] != v2[i])
         return false;
   return true;
}

void solve() {
   int N;
   cin >> N;

   vector<string> v(N);
   for(int i = 0; i < N; i++) {
      cin >> v[i];
   }

   //check if possible
   vector<vector<int> > counts(N);

   vector<char> letters = getLetters(v[0], counts[0]);
   bool good = true;
   for(int i = 1; i < N; i++) {
      vector<char> letters2 = getLetters(v[i], counts[i]);
      if(!same(letters,letters2))
         good = false;
   }   
   if(!good) {
      cout << "Fegla Won";
      return;
   }

   // for each letter determine how many edits
   int ans = 0;
   for(int i = 0; i < counts[0].size(); i++) {
      vector<int> c;
      for(int j = 0; j < N; j++) {
         c.push_back(counts[j][i]);
      }
      sort(c.begin(), c.end());
      int num = c[c.size()-1] - c[0];
      ans += num;
   }

   cout << ans;

}

int main() {

int t;
cin >> t;
for (int i = 0; i < t; i++) {
   cout << "Case #" << i+1 << ": "; 
   solve();
   cout << endl;
}


return 0;
}
