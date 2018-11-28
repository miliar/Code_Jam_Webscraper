#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int cs = 1 ; cs <= T ; cs++){
    int A, N;
    cin >> A >> N;
    vector<int> mote(N);
    for(int i = 0 ; i < N ; i++) cin >> mote[i];
    sort(mote.begin(), mote.end());
    vector<int> v;
    
    for(int i = 0 ; i < N ; i++){
      if(A > mote[i]) A += mote[i];
      else v.push_back(mote[i]);
    }


    int ans = (1<<29);
    sort(v.begin(), v.end());
    for(int i = 0 ; i < v.size() ; i++){ //add
      int n = 1;
      for(int j = 0 ; j < i ; j++) n *= 2;
      int B = ((A-1)*(n)) + 1;
      if(i == 0) B = A;
      int cnt = 0;
      for(int j = 0 ; j < v.size() ; j++){
	if(B > v[j]) B += v[j];
	else cnt++; // remove
      }
      ans = min(ans, i+cnt);
    }
    if(v.size() == 0) ans = 0;
    cout << "Case #" << cs << ": " << ans << endl;
  }
  return 0;
}
