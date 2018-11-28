#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
  int cases;
  cin>>cases;
  for (int z=1;z<=cases;z++) {
    int n;
    int sum=0;
    cin>>n;
    vector<pair<int,int> > v;
    for (int i=0;i<n;i++) {
      int x;
      cin>>x;
      sum+=x;
      v.push_back(make_pair(-x,i));
    }
    cout<<"Case #"<<z<<":";
    while (sum > 0) {
      if (sum==3) {
        sort(v.begin(),v.end());
        cout<<" "<<(char)('A'+v[2].second)<<" "<<(char)('A'+v[0].second)<<(char)('A'+v[1].second);
        break;
      }
      sort(v.begin(),v.end());
      int x=v[0].second;
      v[0].first++;
      sort(v.begin(),v.end());
      int y=v[0].second;
      v[0].first++;
      cout<<" "<<(char)('A'+x)<<(char)('A'+y);
      sum-=2;
    }
    cout<<endl;
  }
  return 0;
}
