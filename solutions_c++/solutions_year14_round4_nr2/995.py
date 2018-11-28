#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int i=1;i<=T;i++){
    int N;
    cin>>N;
    vector<int> v(N);
    for(int i=0;i<N;i++){
      cin>>v[i];
    }
    int c=0;
    for(int i=0;i<N;i++){
      auto it=min_element(begin(v),end(v));
      c+=min(it-begin(v),end(v)-it-1);
      v.erase(it);
    }
    cout<<"Case #"<<i<<": "<<c<<endl;
  }
}

  
    
    
