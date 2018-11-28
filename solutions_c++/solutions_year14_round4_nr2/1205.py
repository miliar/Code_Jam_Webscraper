#include <vector>
#include <iostream>

using namespace std;

int N;

int a[1024];

void scan(){
  cin >> N;
  
  for(int i = 0; i < N; ++i){
    cin >> a[i];
  }
}

inline int ABS(int x){
  return (x < 0)?(-x) : x;
}


void solve(int testCase){
  cout << "Case #" << testCase << ": ";
  int idx = 0, res = 0;
  
  for(int i = 1; i < N; ++i)
    if(a[i] > a[idx])
      idx = i;
  
  int cnt = 0;
  vector<int> v;
  for(int i = idx - 1; i >= 0; --i){
    int l = 0, r = idx - i;
    for(int j = 0; j < i; ++j)
      if(a[j] > a[i])
	++l;
    for(int j = idx + 1; j < N; ++j)
      if(a[j] > a[i])
	++r;
      
    for(int j = 0; j < v.size(); ++j)
      if(v[j] < a[i])
	--r;
    if(l >= r){
      res += r;
      v.push_back(a[i]);
    }
    else{
      res += l;
    }
  }
  cnt = 0;
  int rem = v.size();
  v.erase(v.begin(),v.end());
  for(int i = idx + 1; i < N; ++i){
    int l = 0, r = i - idx;
    for(int j = i + 1; j < N; ++j)
      if(a[j] > a[i])
	++l;
    for(int j = 0; j < idx; ++j)
      if(a[j] > a[i])
	++r;
    for(int j = 0; j < v.size(); ++j)
      if(v[j] < a[i])
	--r;
    if(l >= r){
      res += r;
      v.push_back(a[i]);
    }
    else{
      res += l;
    }
  }
  if(v.size() != 0 && rem != 0){
   // cout << "qwe" << rem << " " << v.size() << endl;
  }
  cout << res  << endl;
}

int main(){
  int tests;
  
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    scan();
    solve(i);
  }
}
