#include <bits/stdc++.h>
using namespace std;

//solved by hand
//x,r,c
//richard = 0, gabriel = 1.
bool a[4][4][4] = {
{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},
{{0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}},
{{0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}},
{{0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}}
};
        

int main() {
  int t;
  cin>>t;
  for(int z=1; z<=t; z++) {
    cout<<"Case #"<<z<<": ";
    int x,r,c;
    cin>>x>>r>>c;
    if(a[x-1][r-1][c-1]) {
      cout<<"GABRIEL"<<endl;
    }
    else cout<<"RICHARD"<<endl;
  }
        
  return 0;
}
