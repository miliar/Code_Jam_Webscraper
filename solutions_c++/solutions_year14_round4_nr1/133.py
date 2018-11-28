#include<cassert>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    int n,x;
    multiset<int> s;
    scanf("%d %d",&n,&x);
    for(int i=0;i<n;i++){
      int x;
      scanf("%d",&x);
      s.insert(x);
    }
    int ans=0;
    while(!s.empty()){
      int largest=*s.rbegin();
      assert(largest<=x);
      int before=s.size();
      s.erase(s.find(largest));
      assert(s.size()==before-1);
      int remaining=x-largest;
      multiset<int>::iterator it=s.upper_bound(remaining);
      while(it!=s.begin()&&(it==s.end()||*it>remaining))--it;
      if(it!=s.end()&&*it<=remaining){
        s.erase(it);
      }
      ++ans;
    }
    printf("Case #%d: %d\n",cc,ans);
  }
}
