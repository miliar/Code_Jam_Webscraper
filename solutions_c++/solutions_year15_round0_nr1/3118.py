#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;
int solve(string s,int l){
int ans=0;
int tot=s[0]-'0';
for(int i=1;i<l;i++){
if(i>tot){
 ans+=(i-tot);
 tot+=(i-tot);
}
tot+=s[i]-'0';
//cout<<i<<"::"<<tot<<"::"<<ans<<endl;
}
return ans;
}
int cse=1;
int main() {
 // freopen("in.txt","r",stdin);
  //freopen("out.txt","w",stdout);
  int n;
  int t;
  cin>>t;
  while(t--){
  string s;
  cin>>n>>s;
    printf("Case #%d: %d\n",cse++,solve(s,n+1));
  }
  return 0;
}
