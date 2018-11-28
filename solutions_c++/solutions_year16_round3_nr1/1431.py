#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
using namespace std;

int main() {
  int tc;
  cin >> tc;
  for(int caseno = 1; caseno <= tc; caseno++) {
    int n;
    cin >> n;
    int vals[40];
    int total = 0;
    for(int i = 0; i < n; i++) {
      cin >> vals[i];
      total += vals[i];
    }
    cout << "Case #" << caseno << ":";
    while(total > 0) {
      // try one
      bool isone = false;
      for(int i = 0; i < n; i++) {
	if(vals[i] > 0){
	  bool isok = true;
	  for(int j = 0; j < n; j++) {
	    int v = vals[j];
	    if(j == i)
	      v--;
	    if(2*v > total-1)
	      isok = false;
	  }
	  if(isok) {
	    vals[i]--;
	    total--;
	    cout << " " <<(char)('A'+i);
	    isone = true;
	    break;
	  }
	}
      }
      if(!isone) {
	bool cont = true;
	for(int i = 0; i < n; i++) {
	  for(int j = i+1; j < n; j++ ){
	    if(vals[i] > 0 && vals[j] > 0) {
	      bool isok = true;
	      for(int k = 0; k < n; k++) {
		int v = vals[k];
		if(k == i || k == j)
		  v--;
		if(2*v > total-2) {
		  isok = false;
		}
	      }
	      if(isok) {
		vals[i]--;
		vals[j]--;
		total -= 2;
		cout << " " << (char)('A'+i) <<(char)('A'+j);
		cont = false;
		break;
	      }
	    }
	  }
	  if(!cont) break;
	}

      }
    
    }
    
    cout << endl;
  }
  return 0;
}
