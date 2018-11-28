#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
using namespace std;
int main() {
  int T;
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cout << "Case #"<<tc<<": ";
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin>>a[i];
    int ans = 0;
    while(a.size() > 0 ){
      int midx = std::min_element(a.begin(),a.end())-a.begin();
      ans = ans  + min<int>(midx, a.size() - midx - 1);
      a.erase(a.begin()+midx);
    }
    cout<<ans<<endl;
  }
}
