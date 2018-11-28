#include <iostream>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

int main(){
  int T;
  cin>>T;
  for (int i=1;i<=T;i++){
    int n;
    cin>>n;
    vector<double> a, b;
    int j;
    double in;
    for (j=0;j<n;j++) {cin>>in; a.push_back(in);}
    for (j=0;j<n;j++) {cin>>in; b.push_back(in);}

    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    vector <double> c (b);
    int wd=0, wod=0;
    int k;
    for (j=n-1;j>=0;j--) {   for (k=c.size()-1;k>=0;k--)
      {if (a[j] >  c[k] ) {wd++; c.erase(c.begin()+k);break;}}}

    for (j=0;j<n;j++) for (k=0;k<b.size();k++) {
      if (b[k]>a[j]) {
	wod++;
	b.erase(b.begin()+k);
	break;
      }
    }
  cout << "Case #"<<i<<": "<< wd <<" "<<n-wod<<endl;
  }
  return 0;
}
