#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t;
ll n;

bool gotall(vector<bool>& got, ll n){
  ll a = n;
  while(a){
    got[a%10] = true;
    a/=10;
  }

  for(int i = 0; i < 10; i++)
    if(got[i] == false)
      return false;
  return true;
}

int main(){

  cin >> t;
  for(int c = 1; c<=t; c++){
    cin >> n;
    vector<bool> got(10, false);
    cout << "Case #" << c << ": ";

    if(n == 0){
      cout << "INSOMNIA" << endl;
      continue;
    }

    ll i = 1;
    while(!gotall(got, n*i)){
      // cout << "n = " << n*i << endl;
      i++;
    }
    cout << n*i << endl;

  }

  return 0;
}
