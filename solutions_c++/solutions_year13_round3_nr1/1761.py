#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <limits>
#include <functional>
#include <queue>
using namespace std;

#define INF (numeric_limits<int>::max() - 1)
int T; 
int main(){
  freopen("input.txt", "r", stdin);
  cin>>T;
  for(int times = 0; times < T; ++times){
    string s;
    int n;
    cin>>s>>n;
    int res = 0;
    for(int i = n; i <= s.size(); ++i){
      for(int j = 0; j <= s.size() - i; ++j){
	bool ok = false;
	int consecutive = 0;
	for(int k = 0; k < i; ++k){
	  if(s[j+k] != 'a' && s[j+k] != 'e' && s[j+k] != 'i' && s[j+k] != 'o' && s[j+k] != 'u'){
	    consecutive++;
	  }
	  else{
	    consecutive = 0;
	  }
	  if(consecutive >= n){
	    ok = true;
	  }
	}
	if(ok){
	  res++;
	}
      }
    }
    cout<<"Case #"<<times + 1<<": "<<res<<endl;
  }
  return 0;
}
