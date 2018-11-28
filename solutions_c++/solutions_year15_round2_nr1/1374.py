#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>
#include <cstring>
#include <cmath>
using namespace std;
int r(int x) {
  int t=0;
  while (x>0) {
    t=t*10+x%10;
    x/=10;
  }
  return t;
}
int main() {
  int zz;
  cin>>zz;
  for (int zzz=1;zzz<=zz;zzz++) {
    set<int> v;
    v.clear();
    int target;
    cin>>target;
    queue<pair<int,int> > q;
    q.push(make_pair(1,1));
    while(!q.empty()) {
      int x=q.front().first;
      int y=q.front().second;
      q.pop();
      if (v.count(x)>0 || y>1000000)
        continue;
      v.insert(x);
      //cout<<x<<" "<<y<<endl;
      if (x==target) {
        printf("Case #%d: %d\n",zzz,y);
        break;
      }
      q.push(make_pair(x+1,y+1));
      q.push(make_pair(r(x),y+1));
    }
  }
  return 0;
}
