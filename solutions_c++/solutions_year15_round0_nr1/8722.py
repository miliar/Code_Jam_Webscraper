#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

int main(){
  int tc,smax;
  string s;
  cin>>tc;
  int ans,standingSoFar;
  for(int tst=1;tst<=tc;tst++){
    cin>>smax>>s;
    ans=standingSoFar=0;
    cout<<"Case #"<<tst<<": ";
    for(int i=0;i<=smax;i++){
      if(standingSoFar>=i){
        standingSoFar+=s[i]-'0';
      } else {
        int need=i-standingSoFar;
        ans+=need;
        standingSoFar+=need+s[i]-'0';
      }
    }
    cout<<ans<<"\n";
  }
  return 0;
}
