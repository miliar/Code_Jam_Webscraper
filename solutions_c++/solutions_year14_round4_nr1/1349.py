#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

const int INF = 1e8;
vector<int>vec;
int N,T,X;

void solve(){
  cin >> N >> X;
  vec = vector<int>(N,0);
  for(int i = 0 ; i < N ; i++)cin >> vec[i];
  sort(vec.begin(),vec.end());
  int l,r;
  l = 0;
  r = N-1;
  int res = 0;
  while(l < r){
    if(vec[l] + vec[r] <= X){
      res++;
      l++;
      r--;
    }
    else{
      res++;
      r--;
    }
  }
  if(l == r)res++;
  
  cout << res << endl;
}

int main(){
  cin >> T;
  for(int i = 1 ; i <= T ; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  
  return 0;
} 
