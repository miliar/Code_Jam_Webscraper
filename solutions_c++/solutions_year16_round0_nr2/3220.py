#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int gcd(int gran, int petit) 
{
  if (petit==0) 
    return gran;
  else
    return gcd(petit,gran%petit);
}

int main() {
  ios_base::sync_with_stdio(false);
  ll t;
  string s;
  cin >> t;
  vector<ll> a(t);
  for (ll i=0; i< t; i++) {
    cin >> s;
    int count=0;
    for (int j=s.size()-1; j>=0; j--)
      if (s[j]=='-') {
	count++;
	for (int l=0; l<j; l++) {
	  if (s[l]=='-')
	    s[l]='+';
	  else
	    s[l]='-';
	}
      }
    a[i]=count;
   }
  for (ll i=0; i< t; i++) {
    cout << "Case #"<<i+1<<": ";
    cout<< a[i]<<"\n";
  }
  return 0;
}
