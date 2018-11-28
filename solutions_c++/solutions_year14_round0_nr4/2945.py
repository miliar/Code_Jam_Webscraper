#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

const double EPS = 1e-8;
int n;
vector<double> va,vb;

bool equal(double a, double b){
  return fabs(a-b) < EPS;
}

void solve(){
  int ansa=n, ansb=0;
  vector<double> va2;
  sort(va.begin(), va.end());
  sort(vb.begin(), vb.end());
  va2 = va;

  /*
  cout << endl;
  for(int i=0;i<va.size();i++) cout << va[i] << ' ';
  cout << endl;
  for(int i=0;i<vb.size();i++) cout << vb[i] << ' ';
  cout << endl;
  */
  
  for(int i=0;i<n;i++){
    vector<double>::iterator it = upper_bound(va2.begin(), va2.end(), vb[i]);
    if(it == va2.end() || *it < vb[i] && !equal(*it,vb[i])) {
      ansa = n - va2.size();
      break;
    }
    else va2.erase(it);
  }

  for(int i=0;i<n;i++){
    vector<double>::iterator it = lower_bound(vb.begin(), vb.end(), va[i]);
    if(it == vb.end() || *it < va[i] && !equal(*it,va[i])) {
      ansb = vb.size();
      break;
    }
    else vb.erase(it);
  }

  cout << ansa << ' ' << ansb << endl;
}

int main(){
  int T;
  double x;
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> n;
    va.clear();
    vb.clear();
    for(int i=0;i<n;i++) {
      cin >> x;
      va.push_back(x);
    }
    for(int i=0;i<n;i++) {
      cin >> x;
      vb.push_back(x);
    }
    cout << "Case #" << t << ": " << flush;
    solve();
  }
}
