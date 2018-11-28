#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int count_bits(int val) {
  int res = 0;
  for(int i =0; i < 30; i++)
    if(val & (1<<i))
      res++;
  return res;
}

int main() {
  int total_cases;
  cin >> total_cases;

  for(int caseno = 1; caseno <= total_cases; caseno++) {
    vector<pair<string, string> > vec;
    vector<int> indxs;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
      string one, two;
      cin >> one >> two;
      vec.push_back(make_pair(one, two));
    }
    int res = 0;
    for(int i = 1; i < (1<<n); i++) {
      bool isok = true;
      for(int j = 0; j < 30; j++) {
	if(i & (1<<j)) {
	  //	  if(i == 4)
	  //	    cout << j << endl;
	  // check j
	  bool first = false;
	  bool second = false;
	  for(int k = 0; k < n; k++) {
	    if( !(i&(1<<k))) {
	      if(vec[j].first.compare(vec[k].first)==0)
		first = true;
	      if(vec[j].second.compare(vec[k].second)==0)
		second = true;
	    }
	  }
	  if(!first || !second) isok = false;
	}
      }

      if(isok)
	res = max(res, count_bits(i));
    }


    cout << "Case #" << caseno << ": " << res << endl;
  }
  return 0;
}
