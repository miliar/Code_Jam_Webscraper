#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
using namespace std;


#define INF (1LL << 60)
typedef long long Int;
typedef pair<Int, Int> P;
Int num[108000];
Int cnt[108000];
int solve(){
  int p;
  cin >> p;
  for(int i = 0;i < p;i++)cin >> num[i];
  for(int i = 0;i < p;i++)cin >> cnt[i];
  vector<int> ans;
  vector<int> ss;
  map<Int, int> dict;
  for(int i = 0;i < p;i++)dict[num[i]] = i;
  ss.push_back(0);
  cnt[0]--;
  for(int i = 0;i < p;){
    if(cnt[i]){
      ans.push_back(num[i]);
      int tmp = ss.size();
      for(int j = 0;j < tmp;j++){
	ss.push_back(ss[j] + num[i]);
	cnt[dict[ss.back()]]--;
      }
    }
    else{
      i++;
    }
  }
  for(int i = 0;i < ans.size();i++){
    if(i)cout << " " ;
    cout << ans[i];
  }cout << endl;
}

int main(){
  Int T;
  cin >> T;
  for(Int t = 1;t <= T;t++){
    cout << "Case #" << t << ": ";
    solve();
  }
  return 0;
}
