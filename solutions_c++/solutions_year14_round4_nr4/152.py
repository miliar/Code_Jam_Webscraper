#include <iostream>
#include <vector>
#include <set>
using namespace std;
int N,M;
vector<string> s;
vector<int> used;
vector<vector<int> > T;

int size(vector<int> k) {
  set<string> ss;
  for(int t:k){
    for(int j = 0; j <= s[t].size(); j++){
      ss.insert(s[t].substr(0,j));
    }
  }
  return ss.size();
}
int max_size, max_cnt;
int dfs(int k, int min = 0) {
  if(k == T.size()) {
    for(int i = 0 ; i < used.size(); i++) {
      if(used[i]==false)return 0;
    }
#if 1
/*
    cout<<"----"<<endl;
    for(int i =0 ;i < T.size();i++){
    for(int j =0 ;j < T[i].size();j++){
      cout<<T[i][j]<<" ";
    }
    cout<<endl;
    }
    */
#endif
    int tans= 0;
    for(int i = 0; i < T.size(); i++) {
      tans+=size(T[i]);
    }
    if(max_size < tans){
        max_size = tans;
        max_cnt = 0;
    }
    
    if(max_size == tans){
      max_cnt += 1;
    }
  }else{
    for(int i = min; i < s.size(); i++){
      if(!used[i]){
        used[i] = true;
        T[k].push_back(i);
        dfs(k, i + 1);
        dfs(k + 1, 0);
        T[k].pop_back();
        used[i] = false;
        //if(min == 0)break;
      }
    }
  }
}
int main() {
  int TT;
  cin>>TT;
  for(int tc=1;tc<=TT;tc++){
    cout<<"Case #" << tc << ": ";
    cin>>M>>N;
    s=vector<string>(M);
    for(int i =0;i<M;i++)cin>>s[i];
    T = vector<vector<int> > (N);
    used= vector<int>(M);
    max_size = 0;max_cnt = 0;
    dfs(0);
    cout << max_size << " " << max_cnt << endl;
  }
}
