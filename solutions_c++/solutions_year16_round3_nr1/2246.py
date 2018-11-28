#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int main() {
  ios_base::sync_with_stdio(false);
  ll t;
  cin >> t;
  int n, j=1;
  vector<pair<int,char> > par;
  long long total, opos;
  while (t--) {
    cin >> n;
    total=0;
    par=vector<pair<int,char> > (n);
    for (int i=0; i<n; i++) {
      cin >> par[i].first;
      total += par[i].first;
      par[i].second='A'+i;
    }
    sort(par.begin(),par.end(), greater<pair<int,char> >());
    cout << "Case #"<<j<<": ";
    j++;
    while (total) {
    sort(par.begin(),par.end(), greater<pair<int,char> >());
    opos=0;
    for (int k=1; k<n; k++)
      opos += par[k].first;
    if (opos < par[0].first) {
      cout << "alarm case "<< j<<endl;
      cout << n<<" " << par[0].first <<" " <<par[1].first<<endl;
    }
    
      if ( (n==2) or ( (n>2) and (par[2].first==0))) {
	  cout << par[1].second<<par[0].second<<" ";
	total -=2;
	continue;
      }
      if (par[0].first>2) {
	cout << par[0].second << " ";
	par[0].first--;
	total --;
	continue;
      }
    
      cout << par[0].second << " ";
      par[0].first--;
      total --;
    }
    cout <<endl;
  }
  return 0;
}
