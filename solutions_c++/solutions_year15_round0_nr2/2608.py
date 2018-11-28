#include <cstdlib>
#include<cstdio>
#include<iostream>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<string.h>
#include<queue>
#include<algorithm>
#include<string.h>
#include <stack>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef unsigned long long ulint;
typedef long long lint;

map<ii,int> mp;

int add(int i, int k) {
  if(i>=k) return 0;
  if(mp.find(ii(i,k))!=mp.end()) return mp[ii(i,k)];
  else mp[ii(i,k)] = 1+add(i,k-i);
  return mp[ii(i,k)];
}

int main()
{
  int T;
  cin>>T;
  for(int i=1;i<=T;i++) {
    int D;
    cin>>D;
    int* P = new int[D];
    for(int i=0;i<D;i++) {
      cin>>P[i];
    }
    sort(P,P+D);
    int mn = 9;
    for(int i=1;i<=9;i++) {
      if(i>=P[D-1] && mn > i) {
        mn = i;
        break;
      } else if(i>=mn) {
        break;
      }
      int x = i;
      for(int j=0;j<D;j++) {
        int k = P[j];
        x+=add(i,k);
      }
      mn = min(mn,x);
    }
    cout<<"Case #"<<i<<": "<<mn<<endl;
  }
}
