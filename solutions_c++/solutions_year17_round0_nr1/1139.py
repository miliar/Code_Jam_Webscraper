//g++ -std=c++14 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define nl '\n'
typedef long long ll;
//////////////////////////////////////////////////////////////////////

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    string s;int k;
    cin>>s>>k;
    cout<<"Case #"<<tt<<": ";
    int n = s.length();
    int ops = 0;
    for(int i=0;i<=n-k;i++)//
      if(s[i]=='-'){
	ops++;
	for(int j=i;j<i+k;j++)s[j]='+'+'-'-s[j];
      }
    bool fail = false;
    for(int i=0;i<n;i++)
      if(s[i]=='-'){fail=true;break;}
    if(fail){cout<<"IMPOSSIBLE"<<nl;continue;}
    cout<<ops<<nl;
  }
  
  return 0;
}
