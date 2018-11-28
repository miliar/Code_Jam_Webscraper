#include <iostream>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0); 
freopen("lighter3.txt", "r", stdin); 
freopen("lighter4.txt", "w", stdout);
int t; cin >> t; 

for (int g=0; g<t; g++){
  string x; cin >> x; 
  x+='+'; int cnt = 0; 
  for (int y=0; y<x.length()-1; y++){
    cnt+=x[y]!=x[y+1]; 
  }cout << "Case #" << g+1 << ": " << cnt << '\n'; 
}

return 0; 
}
