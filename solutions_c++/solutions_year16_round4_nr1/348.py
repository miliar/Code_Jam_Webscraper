#include <bits/stdc++.h>
using namespace std;

int n,r,p,s;
struct so {
  int R,P,S;
  string Z;
};

inline char nx(char c) {
  switch(c) {
  case 'R':
    return 'S';
  case 'P':
    return 'R';
  case 'S':
    return 'P';
  }
  assert(0);
}

so solve(char type, int dep) {
  so ret;
  ret.R=ret.P=ret.S=0;
  if (!dep){
    ret.Z="";
    ret.Z+=type;
    switch(type) {
    case 'R':
      ret.R++;
      break;
    case 'P':
      ret.P++;
      break;
    case 'S':
      ret.S++;
      break;
    }
    return ret;
  }
  so L=solve(type,dep-1);
  so R=solve(nx(type),dep-1);
  ret.R=L.R+R.R;
  ret.S=L.S+R.S;
  ret.P=L.P+R.P;
  ret.Z=min(L.Z,R.Z)+max(L.Z,R.Z);
  //printf("%c %d: %d %d %d ",type,dep,ret.R,ret.S,ret.P);
  //cout<<ret.Z<<endl;
  return ret;
};

int main() {
  int t; cin>>t; for(int zz=1;zz<=t;zz++) {
    cin>>n>>r>>p>>s;
    vector<char> cc{'P','S','R'};
    string ans="zz";
    for(auto c:cc) {
      so q=solve(c,n);
      if(q.R==r&&q.P==p&&q.S==s) ans=min(ans,q.Z);
    }
    if(ans=="zz") printf("Case #%d: IMPOSSIBLE\n",zz);
    else printf("Case #%d: ",zz), cout<<ans<<endl;
  }
}
