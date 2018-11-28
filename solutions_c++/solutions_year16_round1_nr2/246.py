#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main(int argc, const char * argv[]){
  int TT;cin >> TT;
  for(int ii=0;ii<TT;ii++){
int N;
cin >>N;
map<int,int> mymap;
for(int i=0;i<2*N-1;i++){
  for(int j=0;j<N;j++){
    int X;cin >> X;mymap[X]++;
  }
}
cout << "Case #"<<ii+1<<": ";
for(auto i:mymap){
  if(i.second%2==1)cout << i.first<<" ";
}
cout << endl;
}
}
