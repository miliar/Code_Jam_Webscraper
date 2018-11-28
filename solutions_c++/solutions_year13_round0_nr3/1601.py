#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lli;

vector<lli> data;
const lli N = (lli)1e+14;

void init(){
  for(lli i=1;;i++){
    if(i * i > N) break;
    lli t = i;
    vector<int> tmp;
    while(t){
      tmp.push_back(t % 10);
      t /= 10;
    }
    int s = tmp.size();
    bool f = true;
    for(int j=0;j<s;j++) if(tmp[j] != tmp[s-1-j]) f = false;
    if(!f) continue;
    t = i * i;
    tmp.clear();
    while(t){
      tmp.push_back(t % 10);
      t /= 10;
    }
    s = tmp.size();
    f = true;
    for(int j=0;j<s;j++) if(tmp[j] != tmp[s-1-j]) f = false;
    if(f) data.push_back(i*i);
  }
}

lli calc(lli a, lli b){
  return upper_bound(data.begin(), data.end(), b) - lower_bound(data.begin(), data.end(), a);
}

main(){
  int T;
  cin >> T;
  init();
  for(int t=1;t<=T;t++){
    lli a, b;
    cin >> a >> b;
    cout << "Case #" << t << ": " << calc(a, b) << endl;
  }
}
