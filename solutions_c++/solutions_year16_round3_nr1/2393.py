#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
  int t; cin >> t; 
  for(int cse = 1; cse <=t ; cse ++){
    cout<<"Case #"<<cse<<": ";
    int n;
    cin >> n ;
    vector<pair<int,char> > v; 
    for(int i =0 ; i < n ; i ++) {
      int x ;
      cin >>x;
      v.push_back(make_pair(x, 'A'+i));
    }
    int index = 0, rem = n;
    while(1){
      sort(v.begin(), v.end());
      if(v[n-1].first == 0 ) break;
      int cnt = 0 ;
      for(int i =0 ; i <n ; i ++ ) cnt += v[i].first > 0;

      if(v[n-1].first > v[n-2].first or cnt == 3){
        cout<<v[n-1].second<<" ";
        v[n-1].first --;
        continue;
      }

      cout<<v[n-1].second<<v[n-2].second<<" "; 
      v[n-2].first--;
      v[n-1].first--;
    }
    cout<<endl;
  }
}
