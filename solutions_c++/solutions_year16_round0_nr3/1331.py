#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


int n,j,counter = 0;
int state[50];
set<ll> s;

void dfs(int d,int step){
  if(counter == j){
    return;
  }
  if(d == n+1){
    ll num = 1;
    ll check = 0;
    for(int i = 1;i <= n;++i){
      check += num*state[i];
      num *= 2;
    }
    if(s.find(check) != s.end()){
      return;
    }
    s.insert(check);
    for(int i = 1;i <= n;++i){
      cout << state[i];
    }
    for(int i = 2;i <= 10;++i){
      cout << " " << (int)pow(i,step) + 1;
    }
    cout << endl;
    ++counter;
  }else{
    dfs(d+1,step);
    if(state[d] == 0 &&
       state[d+step] == 0){
      state[d] = 1;
      state[d+step] = 1;
      dfs(d+1,step);
      state[d] = 0;
      state[d+step] = 0;
    }
  }
  return;
}

int main(void){
  int t;
  cin >> t;
  cin >> n >> j;
  fill(state,state+50,0);
  state[1] = 1;state[n] = 1; 
  puts("Case #1:");
  for(int i = 1;i < n-1;++i){
    if(counter == j)break;
    state[1+i] = 1;
    state[n-i] = 1;
    dfs(1,i);
    state[1+i] = 0;
    state[n-i] = 0;
  }
  //cout << counter << endl;
  return 0;
}
