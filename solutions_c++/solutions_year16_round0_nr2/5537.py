#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
void solve() {
  string s;
  cin>>s;
  int n=s.size();
  int cnt=0;
  int left=0;
  reverse(s.begin(), s.end());
  while(true) {
    while(left<n && s[left]=='+') ++left;
    if(left>=n) break;
    int right=n;
    while(s[right-1]=='+')s[--right]='-';
    if(right<n) {
      ++cnt;
    }
    reverse(s.begin()+left,s.end());
    for(int i=left;i<n;++i) s[i]=s[i]=='+'?'-':'+';
    ++cnt;


    
    
  }
  cout<<cnt<<endl;
}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    solve();
  }

}
