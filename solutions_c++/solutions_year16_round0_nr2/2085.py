#include<bits/stdc++.h>
#define ft first
#define sd second
#define pb push_back
using namespace std;

typedef long long ll;

const int N = 1100000;

int main(){
  ios_base::sync_with_stdio(0);
  int t;
  cin>>t;
  for(int tt = 1; tt <= t; tt++){
    string s;
    cin >> s;
    s += '+';
    int n = s.length();
    int k = 0;
    for(int i = 1; i < n; i++) if(s[i-1] != s[i]) k++;
    cout << "Case #"<< tt << ": " << k << "\n";
  }
}