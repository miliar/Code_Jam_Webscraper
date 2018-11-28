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
  cin >> t;
  for(int tt = 1; tt <= t; tt++){
    ll k, c, s;
    cin >> k >> c >> s;
    if(c * s < k){
      cout << "Case #" << tt << ": IMPOSSIBLE\n";
      continue;
    }
    cout << "Case #" << tt << ": ";
    vector<ll> pot(110);
    pot[0] = 1;
    for(int i = 1; i <= c; i++) pot[i] = pot[i-1] * k;
    ll wyn = 0;
    for(int i = 0; i < k; i++){
      ll r = i % c;
      wyn += pot[r] * i;
      if(r == c - 1 or i == k - 1){
	cout << wyn + 1 << " ";
	wyn = 0;
      }
    }
    cout<<"\n";
  }   
}