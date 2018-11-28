#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
 int t; cin>>t;
 for (int c=1; c<=t; c++) {
  int d; cin>>d;
  vector<int> p(d);
  int pmax=0;
  for (int i=0; i<d; i++) cin>>p[i], pmax=max(pmax,p[i]);
  int ret=1e9;
  for (int lim=1; lim<=pmax; lim++) {
   int cur=0, rem=0;
   for (int i=0; i<d; i++) {
    cur+=(p[i]-1)/lim;
    int tmp=p[i]%lim;
    if(p[i]>=lim) tmp=lim;
//    cout << lim << ": " << i << " :: " << cur << " " << tmp << endl;
    rem=max(rem,tmp);
   }
   ret=min(ret,cur+rem);
  }
  cout << "Case #" << c << ": " << ret << endl;
 }
 return 0;
}

