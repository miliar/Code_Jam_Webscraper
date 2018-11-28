#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;
int solve();
int main(){

  int T;
  cin>>T;
  for (int i = 0; i < T; ++i){
    cout<<"Case #"<<i+1<<": "<<solve()<<endl;
   
  }
}
int solve(){
  int palsarr[5] = {1, 4, 9, 121,484};
  vector <int> pals;
  pals.assign(palsarr,palsarr+5);
  
  int A,B; 
  cin>>A>>B;
  vector<int>::iterator itA = lower_bound(pals.begin(),pals.end(),A);
  vector<int>::iterator itB = upper_bound(pals.begin(),pals.end(),B);
  return (itB-itA);
}
