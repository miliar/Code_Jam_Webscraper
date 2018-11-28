#include <cstdio>
#include <queue>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cstring>
#include <cmath>
using namespace std;

int N;
int main () {
  int T;
  scanf("%d",&T);
  
  for(int t = 1 ; t <= T; ++t) {
    scanf("%d\n",&N);
    
    vector<pair<char, vector<int> > >strs;
    
    bool fail = false;
    
    for(int i = 0; i< N; ++i){
      char buf [150];
      gets(buf);
      
      if(fail)
	continue;
      
      char c = buf[0]; int accnt = 1, pos = 0;
      for(int j = 1; j < strlen(buf); ++j) {
	if(buf[j] != c) {
	  if(pos >= strs.size()) {
	    if(i) {
	      fail = true;
	      break;
	    }
	    strs.push_back(pair<char,vector<int> >(0,vector<int>()));
	  }
	  if(i == 0)
	    strs[pos].first = c;
	  else
	    if (strs[pos].first != c) {
	      fail = true;
	      break;
	    }
	  strs[pos].second.push_back(accnt);
	  ++pos;
	  c = buf[j];
	  accnt = 1;
	}
	else
	  accnt++;
      }
      if(pos >= strs.size()){
	if(i) {
	  fail = true;
	  break;
	}
	strs.push_back(pair<char,vector<int> >(0,vector<int>()));
      }
      if(i == 0)
	strs[pos].first = c;
      else
	if (strs[pos].first != c) {
	  fail = true;
	  continue;
	}
      
      if(pos != strs.size() - 1)
	fail = true;
	
      if(!fail) {
	strs[pos].second.push_back(accnt);
	++pos;
	accnt = 1;
      }
    }
    printf("Case #%d: ", t);
    
    if(fail) {
      printf("Fegla Won\n");
    }
    else {
      int cnt = 0;
      
      for(auto i : strs){
	int ds = 0;
	for(auto j : i.second)
	  ds+=j;
	ds /= N;
	
	for(auto j : i.second)
	  cnt += (abs (j - ds));
      }
      printf("%d\n",cnt);
    }
  }
}

