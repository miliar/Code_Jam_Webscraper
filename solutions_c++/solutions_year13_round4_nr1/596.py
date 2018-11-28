#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <cctype>
#include <algorithm>
#include <tr1/tuple>
using namespace std;
using namespace std::tr1;

typedef __int128_t INT;

const INT modd = 1000002013;
const int MAX_N = 1030;

int do_case(){
  int N,M;
  
  map<int,vector<pair<int,int> > > off;
  map<int,int> ticks,on;
  
  INT curr = 0;
  
  long long E,O,PP;
  cin >> N >> M;
  for(INT i=0;i<M;i++){
    cin >> E >> O >> PP;
    
    INT d = O-E,p = PP;
    curr += p * (d*N - (d*(d-1))/2);
    curr %= modd;
    
    on[E] += PP;
    on[O] += 0;
    
    off[O].push_back(make_pair(E,PP));
    off[E].push_back(make_pair(E,0));
  }
  
  INT ans = 0;
  
  for(map<int,int>::iterator it=on.begin();it!=on.end();++it){
    INT loc = it->first;
    
    // getting on
    ticks[loc] += it->second;
    
    // getting off
    if(off.count(loc) == 0) continue; // no one

    sort(off[loc].begin(),off[loc].end());
    
    for(int i=0;i<off[loc].size();i++){
      int rid_of = off[loc][i].second;
      map<int,int>::reverse_iterator it1;
      for(it1=ticks.rbegin();rid_of > 0 && it1!=ticks.rend();++it1){
	int val = (it1->second > rid_of ? rid_of : it1->second);
	int d = loc-(it1->first);
	ans += val * (d*N - (d*(d-1))/2);
	ans %= modd;
	it1->second -= val;
	rid_of -= val;
      }
    }
    start:
    map<int,int>::iterator it=ticks.end();
    for(it--;it!=ticks.begin() && it->second == 0;){
      ticks.erase(it);
      goto start;
    }
  }
  
  INT val = (curr-ans) % modd;
  if(val < 0) val += modd;
  return val;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--)
    cout << "Case #" << C++ << ": " << do_case() << endl;
  return 0;
}
