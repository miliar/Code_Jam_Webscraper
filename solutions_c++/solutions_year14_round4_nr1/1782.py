#include <climits>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>

using namespace std;


void run(int case_index) {
  int n,x; cin >> n >> x;
  multiset<int> s;
  for (int i = 0; i < n; i++) {
    int v; cin >> v;
    s.insert(v);
  }
  ;
  

  
  int res=0;
  multiset<int>::reverse_iterator i;
  while(!s.empty()){
    if(s.size() == 1){
      res++; 
      break;
    }
    else{
      i = s.rbegin();
      int v = *i;
      multiset<int>::iterator it0 = lower_bound(s.begin(), s.end(), v);
      s.erase(it0);
      multiset<int>::iterator it;
      it = upper_bound(s.begin(), s.end(), x - v);
      if(it == s.begin()){
        
      }
      else{
        it--;
        s.erase(it);
      }
      res++;
    }
    


  }
  
  cout << "Case #" << case_index << ": " << res;
  cout << endl;
}

int main(int argc, char* argv[]) {
  int n; 
  cin >> n;
  for(int i = 1; i <= n; i++){
    cerr << i << " ";
    run(i);
  }
  cerr << endl;
  return 0;
}
