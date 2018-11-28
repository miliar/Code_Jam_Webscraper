#include <bits/stdc++.h>

using namespace std;

map< vector<int>, int> done;

int check(vector<int> x){
  sort(x.begin(),x.end());
  if( done.count(x) == 0 )
    return -1;
  else
    return done[x];
}

void save(vector<int> arr, int val){
  sort(arr.begin(),arr.end());
  done[arr] = val;
}

int solve(vector<int> arr){
  //cout << (int) arr.size() << endl;
  //std::copy(arr.begin(),arr.end(),std::ostream_iterator<int>(std::cout<< " " ));
  //cout << endl;
  
  int _tmp = check(arr);
  if( _tmp != -1 )
    return _tmp;

  bool allzeros = true;
  for(int i=0;i<(int)arr.size() && allzeros;i++)
    allzeros &= (arr[i] == 0);
  if( allzeros )
    return 0;
  int n = arr.size();
  vector<int> tmp = vector<int>(arr.begin(),arr.end());
  for(int i=0;i<n;i++)
    if(tmp[i])
      tmp[i]--;
  int ans = 1+solve(tmp);
  for(int i=0;i<n;i++){
    for(int j=2;j<=arr[i]/2;j++){
      tmp = vector<int>(arr.begin(),arr.end());
      int val = tmp[i];
      //cout << val << " " << val -j << " " << val - (val-j) << endl;
      tmp.erase(tmp.begin()+i);
      tmp.push_back(val-j);
      tmp.push_back(val - (val-j));
      ans = min(ans, 1+solve(tmp));
    }
  }
  save(arr, ans);
  return ans;
}

int main(){
  freopen("b2.in", "r", stdin);
  freopen("b3.out", "w", stdout);
  int t;
  cin >> t;
  int tc = 1;
  while(t--){
    int n;
    cin >> n;
    vector<int> arr;
    for(int i=0;i<n;i++){
      int tmp;
      cin >> tmp;
      arr.push_back(tmp);
    }
    cout << "Case #" << tc++ << ": " << solve(arr) << endl;
  }
}
