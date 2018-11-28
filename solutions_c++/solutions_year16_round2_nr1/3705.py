#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define _f(i,x,n) for(int i=x;i<n;i++)
#define _if(i,x,n) for(int i=(n);i>=x;i--)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

string nums[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

string getNumber(string S, int idx){
  if(9 < idx && 0 < S.size())
    return "-";
  else if(9 < idx || S.empty())
    return "";

  string bck = S;
  //_dv(S)_dv(idx)
  bool found = true;
  _f(k, 0, nums[idx].size()){
    int pos = S.find_first_of(nums[idx][k]);
    if(pos != string::npos){
      S.erase(pos, 1);
    }
    else{
      found = false;
      S = bck;
      break;
    }
  }
  //_dv(S)
  //if number is found
  if(found){
    stringstream ss;
    ss<<idx;
    
    if(S.empty())
      return ss.str();
    
    //_ln
    string res = getNumber(S, idx);
    //_dv(res)
    if(res.find_first_of('-') != string::npos){
      return getNumber(bck, idx + 1);
    }
    else
      ss<<res;
    return ss.str();
  }
  else{
    //_ln
    string yy = getNumber(S, idx+1);
    //_dv(yy)
    return yy;
  }
}


int main(){
  int T;
  string S, bck;
  
  cin>>T;
  _f(tt,1,T+1){
    cout<<"Case #"<<tt<<": ";
    cin>>S;
    string res = getNumber(S, 0);
    cout<<res<<endl;
  }
  
  return 0;
}

