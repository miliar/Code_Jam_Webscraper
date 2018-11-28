#include <iostream>
#include <cmath>
#include <map>
#include <utility>
#include <iomanip>
#include <vector>
#include <string>
using namespace std;

int change(vector<string> &v){
  vector<vector<int> > vv;
  string s0,s;
  int count,num,num1,num2,mid;
  for (int j=0; j<v.size(); j++){
    vector<int> vi;
    string s;
    s += v[j][0];
    count=1;
    for (int i=1;i<v[j].size(); i++){
      if (v[j][i]==s[s.length()-1]){
        count++;
      }
      else{
        vi.push_back(count);
        s+=v[j][i];
        count = 1;
      }
    }
    vi.push_back(count);
    vv.push_back(vi);
    if (j==0){
      s0 = s;
    }
    if (s.compare(s0)!=0) return -1;
  }
  num = 0;
  for (int i=0; i<s0.length(); i++){
    mid = 0;
    for (int j=0; j<vv.size(); j++){ 
      mid += vv[j][i];
    }
    mid /= vv.size();
    num1 = 0;
    for (int j=0; j<vv.size(); j++){ 
      num1 += abs(vv[j][i]-mid);
    }
    mid++;
    num2 = 0;
    for (int j=0; j<vv.size(); j++){ 
      num2 += abs(vv[j][i]-mid);
    }
    num += min(num1,num2);
  }
  return num;
}

int main(){
  int ti,i,j,k,n,m;
  vector<string> v;
  string s;
  cin>>ti;
  for (i=1; i<=ti; i++){
    if (i>1) cout << endl;
    cout << "Case #" << i << ": ";
    cin>>m;
    v.clear();
    for (j=0; j<m; j++){
      cin>>s;
      v.push_back(s);
    }
    n = change(v);
    if (n>=0)
      cout << n;
    else
      cout << "Fegla Won";
  }
  return 0;
}

