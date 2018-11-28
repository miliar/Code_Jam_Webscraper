#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long lli;
const lli MAX = 100000000000000;
vector<lli> v;

bool isP(lli a){
  vector<lli> v2;
  while(a > 0){
    v2.push_back(a%10);
    a /= 10;
  }
  for(int i=0;i<v2.size()/2;i++)
    if(v2[i] != v2[v2.size()-i-1])
      return false;
  return true;
}

void init(){
  for(lli i=1;i*i<=MAX;i++)
    if(isP(i) && isP(i*i))
      v.push_back(i*i);
}

int main(){
  int T;
lli a,b;
  init();
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> a >> b;
    cout << "Case #" << t << ": " << upper_bound(v.begin(),v.end(),b) - lower_bound(v.begin(),v.end(),a) << endl;
  } 
}
