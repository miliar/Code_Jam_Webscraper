#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<complex>
#include<numeric>
#include<set>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<utility>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<climits>
#include<cfloat>
#include<cassert>

using namespace std;

typedef long long LL;

struct Mote{
  vector<int> m;
  int k;
  Mote(vector<int> _m,int _k){m=_m;k=_k;}
};

bool check(int a,vector<int> v){
  int n=v.size();
  int A=a;
  for(int i=0;i<n;i++){
    if(A<=v[i])return false;
    a+=v[i];
  }
  return true;
}
int main(){
  int CaseT;
  cin>>CaseT;
  for(int Case=1;Case<=CaseT;Case++){
    printf("Case #%d: ",Case);
    int A,N;
    cin>>A>>N;
    vector<int> mote;
    for(int i=0;i<N;i++){
      int n;
      cin>>n;
      mote.push_back(n);
    }
    sort(mote.begin(),mote.end());
    int ans=0;
    queue<Mote> Q;
    Q.push(Mote(mote,0));
    while(!Q.empty()){
      Mote tmp=Q.front();Q.pop();
      mote=tmp.m;
      int n=mote.size();
      int sum=A;
      bool flag=true;
      for(int i=0;i<n;i++){
        if(sum<=mote[i]){
          mote.push_back(sum-1);
          sort(mote.begin(),mote.end());
          Q.push(Mote(mote,tmp.k+1));
          flag=false;
          break;
        }
        sum+=mote[i];
      }
      if(flag){
        ans=tmp.k;
        break;
      }
      mote=tmp.m;
      mote.pop_back();
      Q.push(Mote(mote,tmp.k+1));
    }
    printf("%d\n",ans);
  }
  return 0;
}