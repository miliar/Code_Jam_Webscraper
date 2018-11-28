#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <bitset>

using namespace std;

void solve() {
   int N, X;
   cin >> N >> X;

   vector<int> v(N);
   for (int i = 0; i<N; i++) {
      cin >> v[i];
   }
   sort(v.begin(), v.end());
   reverse(v.begin(), v.end());
   set<int> removed;
   int count = 0;
   vector<int> spaces;
   for(int i = 0; i < N; i++) {
      int smallest = X;
      int index = -1;
      for(int j = 0; j < spaces.size(); j++) {
         if(spaces[j] >= v[i]){
            smallest = min(smallest,spaces[j]);
            index = j;
         }
      }
      if(smallest < X){
         spaces.erase(spaces.begin()+index);
      }
      else {
         spaces.push_back(X-v[i]);
         count++;
      }
   }
   cout<<count;


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
