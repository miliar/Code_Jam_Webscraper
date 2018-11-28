//g++ -std=c++11 ./SC.cpp -o ./p
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define pf push_front
#define ff first
#define ss second
#define rz resize

typedef long long ll;
typedef pair<int,int> pii;

int main(){
  ios::sync_with_stdio(0),cin.tie(0);

#ifndef ONLINE_JUDGE
  freopen("i","r",stdin);
  freopen("o","w",stdout);
#endif

  ll T,N,K,i;
  cin>>T;
  for(int t = 1;t <= T;++t){
    cin>>N;
    cout<<"Case #"<<t<<": ";
    if(N==0){
      cout<<"INSOMNIA"<<endl;
      continue;
    }

    set<int> S;
    for(i=1;S.size()<10;i++){
      K=N*i;
      while(K){
	S.insert(K%10);
	K/=10;
      }
    }

    cout << N*(i-1) << endl;

  }
  return 0;
};
