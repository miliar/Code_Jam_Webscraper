#include<bits/stdc++.h>
using namespace std;

int N,T;
int F[55];
vector<int> v;
bool check( ){
  for(int i=0;i<(int)v.size();i++){
    int pr = v[(i+(int)v.size()-1)%(int)v.size()];
    int nx = v[(i+1)%(int)v.size()];
    if( F[v[i]] != pr && F[v[i]] != nx ) return false;
  }
  return true;
}

bool solve(int st){  
  if( st == (1<<N)-1 ) return check();
  for(int i=0;i<N;i++){
    if( st & (1<<i) ) continue;
    v.push_back( i );
    if( solve(st|(1<<i)) ) return true;
    v.pop_back();
  }
  return false;
}


int main(){
  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){
    cout << "Case #" << ttt << ": ";
    cin >> N;
    vector<int> V;
    for(int i=0;i<N;i++){
      cin >> F[i]; F[i]--;
    }

    int res = 0;
    for(int i=0;i<(1<<N);i++){
      int n = N-__builtin_popcount(i);
      if( n <= res ) continue;
      v.clear();
      if( solve(i) ) res=max(res,n);
    }
    cout << res << endl;
  }
}
