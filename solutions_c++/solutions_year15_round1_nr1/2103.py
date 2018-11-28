#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main() {
  int T;cin>>T;
  for (int t=1;t<=T;++t){
    cout<<"Case #"<<t<<": ";
    int N;cin>>N;
    vector<int> M;
    long long y=0,z=0;
    for (int i=0;i<N;++i){
      int x;cin>>x;
      M.push_back(x);
    }
    long long rate=0;
    for (int i=1;i<N;++i){
      if (M[i]<M[i-1]) {
        int t=M[i-1]-M[i];
        y += t;
        rate = (rate<t)?t:rate;
      } 
    }
    for (int i=0;i<N-1;++i){
      z += (M[i]>rate)?rate:M[i];
    }
    cout<<y<<" "<<z<<endl;
  }
  return 0;
}
