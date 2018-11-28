#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <bitset>

using namespace std;

int countswaps(const vector<int> &v,vector<int> &order){
int count = 0;
for(int i = 0; i<v.size(); i++) {
   if(v[i]!=order[i]) {
      for(int j=i+1;j<order.size();j++)
         if(order[j]==v[i]){
            for(int k = j; k>=i+1;k--){
               swap(order[k],order[k-1]);
               count++;
            }
            break;
         }

   }

}

return count;
}

void solve() {
   int N;
   cin >> N;
   vector<int> v(N);
   for(int i = 0; i<N; i++)
      cin>>v[i];

   int minswaps = N*N;
   vector<int> order = v;
   sort(order.begin(), order.end());
 do{
   vector<int> vv = order;
   bool increasing=true;
   bool bad = false;
   for(int i = 0; i < N-1; i++) {
      if(increasing){
         if(vv[i]>vv[i+1])
            increasing = false;
      }
      else if(vv[i]<vv[i+1]){
         bad = true;
         break;
      }
   }
   if(bad)
      continue;

   minswaps = min(minswaps, countswaps(v,vv));
 }
 while(next_permutation(order.begin(),order.end()));
cout<<minswaps;
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
