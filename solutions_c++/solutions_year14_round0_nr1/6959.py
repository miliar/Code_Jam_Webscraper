#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <string.h>
using namespace std;
int main(){
  freopen("small.in", "r", stdin);
  int T, a, b;
  cin>>T;
  for(int times = 1; times <= T; ++times){
    cin>>a;
    int arr1[4][4];
    int card = 0;
    memset(arr1, sizeof(arr1), 0);
    for(int i = 0; i < 4; ++i){
      for(int j = 0; j < 4; ++j){
	cin>>card;
	arr1[i][j] = card;
      }
    }
    cin>>b;
    int arr2[4][4];
    memset(arr2, sizeof(arr2), 0);
    for(int i = 0; i < 4; ++i){
      for(int j = 0; j < 4; ++j){
	cin>>card;
	arr2[i][j] = card;
      }
    }
    a--, b--;
    int cnt = 0;
    set<int> s;
    for(int i = 0; i < 4; ++i){
      s.insert(arr1[a][i]);
    }
    int res = 0;
    for(int i = 0; i < 4; ++i){
      if(s.find(arr2[b][i]) != s.end()){
	res = arr2[b][i];
	cnt++;
      }
    }
    cout<<"Case #"<<times<<": ";
    if(cnt == 1){
      cout<<res<<endl;
    }
    else if(cnt == 0)cout<<"Volunteer cheated!"<<endl;
    else if(cnt > 1)cout<<"Bad magician!"<<endl;
  }
  return 0;
}
