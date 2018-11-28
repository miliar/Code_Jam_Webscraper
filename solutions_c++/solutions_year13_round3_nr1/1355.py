#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
#define ull unsigned long long
int T,lst,n;
string s;
ull ans;
bool check(int a,int b){
  for(int i=a;i<=b;i++){
    if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
      return false;
  }
  return true;
}
void solve(){
  int len=s.length();
  string temp;
  for(int i=0;i+n-1<len;i++){
    if(check(i,i+n-1)){
      if(lst==-1){
        ans+=(i+1)*(len-(i+n-1));
      }else{
        ans+=(i-lst)*(len-(i+n-1));
      }
      lst=i;
    }
  }
}
int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    lst=-1;
    ans=0;
    printf("Case #%d: ",tc);
    cin>>s>>n;
    solve();
    cout<<ans<<endl;
  }
  return 0;
}
