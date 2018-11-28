#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
//--
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<sstream>
#define X first
#define Y second
#define pb push_back
#define pqPair priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >
#define all(X) (X).begin(),(X).end()

using namespace std;
typedef __int64 ll;

int solve(vector<int>a,vector<int> b){
  int i,j,k,re=0;
  for(i=0;i<a.size();i++){
    j=i;
    while(b[i]!=a[j])j++;
    for(;j>i;j--){
      swap(a[j],a[j-1]);
      re++;
    }
  }
  return re;
}

int main(){
  int t,T;
  cin>>T;
  for(t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    int i,j,k;
    int N,mx=-1,mp;
    cin>>N;
    vector<int> aa(N),a;
    for(i=0;i<N;i++){
      cin>>aa[i];
      if(mx<aa[i]){
        mx=aa[i];
        mp=i;
      }
    }
    for(i=0;i<N;i++)
      if(i!=mp)
        a.pb(aa[i]);
    vector<int> l,r,b;
    int re=1000;
    for(i=0;i<(1<<(N-1));i++){
      l.clear();r.clear();
      for(j=0;j<N-1;j++){
        if((i>>j)%2)
          l.pb(a[j]);
        else
          r.pb(a[j]);
      }
      sort(l.begin(),l.end());
      sort(r.begin(),r.end());
      l.pb(mx);
      for(j=r.size()-1;j>=0;j--)
        l.pb(r[j]);
     /* for(j=0;j<N;j++)
        cout<<l[j]<<" ";
      cout<<endl;*/
      re=min(re,solve(aa,l));
    }
    cout<<re<<endl;
  }
  return 0;
}