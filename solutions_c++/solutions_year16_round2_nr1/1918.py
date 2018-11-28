#include <bits/stdc++.h>
using namespace std;
void solve();
multiset<int> ans;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    for (int i=0; i<t; i++) {
      string s;
      ans.clear();
      int Hash[300] = {0};
      cin>>s;
      for (int j=0; j<s.size(); j++) {
        Hash[s[j]]++;
      }

      while (Hash['Z']) {
        ans.insert(0);
        Hash['Z']--;
        Hash['E']--;
        Hash['R']--;
        Hash['O']--;
      }
      //TWO
      while (Hash['T'] && Hash['W'] && Hash['O']) {
        ans.insert(2);
        Hash['T']--;
        Hash['W']--;
        Hash['O']--;
      }

      //SIX
      while (Hash['S'] && Hash['I'] && Hash['X']) {
        ans.insert(6);
        Hash['S']--;
        Hash['I']--;
        Hash['X']--;
      }

      //eight
      while (Hash['G']) {
        ans.insert(8);
        Hash['E']--;
        Hash['I']--;
        Hash['G']--;
        Hash['H']--;
        Hash['T']--;
      }

      //four
      while (Hash['U']) {
        ans.insert(4);
        Hash['F']--;
        Hash['O']--;
        Hash['U']--;
        Hash['R']--;
      }


      //one
      while (Hash['O']) {
        ans.insert(1);
        Hash['O']--;
        Hash['N']--;
        Hash['E']--;
      }
      
      //3
      while (Hash['H']) {
        ans.insert(3);
        Hash['T']--;
        Hash['H']--;
        Hash['R']--;
        Hash['E']--;
        Hash['E']--;
      }

      //5
      while (Hash['F']) {
        ans.insert(5);
        Hash['F']--;
        Hash['I']--;
        Hash['V']--;
        Hash['E']--;
      }

      //7
      while (Hash['S']) {
        ans.insert(7);
        Hash['S']--;
        Hash['E']--;
        Hash['V']--;
        Hash['E']--;
        Hash['N']--;
      }

      //9
      while (Hash['N']) {
        ans.insert(9);
        Hash['N']--;
        Hash['I']--;
        Hash['N']--;
        Hash['E']--;
      }
      cout<<"Case #"<<i+1<<": ";
      for (auto elem : ans) {
        cout<<elem;
      }
      cout<<endl;
    }
    return 0;
}

