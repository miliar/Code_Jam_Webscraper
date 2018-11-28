#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
using namespace std;

int DEBUG;

string doit(vector<int> v) {
  string ret="";
  for(int z=0;z<10000;z++) {
    int ct=0;
    for(int i=0;i<v.size();i++) ct+=v[i];
    if(ct==0) break;
    vector<pair<int,int> > sorted;
    for(int i=0;i<v.size();i++) sorted.push_back(make_pair(v[i],i));
    sort(sorted.begin(),sorted.end());
    reverse(sorted.begin(),sorted.end());
    if(ret.size()) ret=ret+" ";
if(DEBUG) for(int i=0;i<sorted.size();i++) cout<<"*"<<sorted[i].first<<" "<<sorted[i].second<<endl;
    if(sorted[1].first*2>ct-1&&sorted[1].first>0) { 
      ret+=string(1,(char)('A'+sorted[0].second))+string(1,(char)('A'+sorted[1].second)); 
      v[sorted[0].second]--; v[sorted[1].second]--;
    }
    else { 
      ret+=string(1,(char)('A'+sorted[0].second)); 
      v[sorted[0].second]--;
    }
if(DEBUG)    cout<<v[0]<<" "<<v[1]<<" "<<v[2]<<" "<<ret<<endl;
  }
  return ret;
}

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    int n;
    cin>>n;
    vector<int> v;
    for(int j=0;j<n;j++) {
      int ct; cin>>ct; v.push_back(ct);
    }
DEBUG=(i==1123);
    cout<<"Case #"<<(i+1)<<": "<<doit(v);
    cout<<endl;
  }
  return 0;
}
