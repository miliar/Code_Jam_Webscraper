#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int T,C,n,R,P,S,flag;string ans;
string dfs(int x,char o){
  string t="";
  if(x==n){
    t+=o;
    return t;
  }
  if(o=='R'){
    string l=dfs(x<<1,'R'),r=dfs(x<<1,'S');
    if(l>r)swap(l,r);
    return l+r;
  }
  if(o=='P'){
    string l=dfs(x<<1,'P'),r=dfs(x<<1,'R');
    if(l>r)swap(l,r);
    return l+r;
  }
  if(o=='S'){
    string l=dfs(x<<1,'S'),r=dfs(x<<1,'P');
    if(l>r)swap(l,r);
    return l+r;
  }
}
bool check(string t){
  int cr=0,cp=0,cs=0;
  for(int i=0;i<n;i++){
    if(t[i]=='R')cr++;
    if(t[i]=='P')cp++;
    if(t[i]=='S')cs++;
  }
  return cr==R&&cp==P&&cs==S;
}
int main(){
  cin>>T;
  for(C=1;C<=T;C++){
    cin>>n>>R>>P>>S;
    n=1<<n;
    flag=0;
    string now=dfs(1,'R');
    if(check(now)){
      if(!flag){flag=1;ans=now;}
      else if(ans>now)ans=now;
    }
    now=dfs(1,'P');
    if(check(now)){
      if(!flag){flag=1;ans=now;}
      else if(ans>now)ans=now;
    }
    now=dfs(1,'S');
    if(check(now)){
      if(!flag){flag=1;ans=now;}
      else if(ans>now)ans=now;
    }
    if(flag)cout<<"Case #"<<C<<": "<<ans<<endl;
    else cout<<"Case #"<<C<<": IMPOSSIBLE"<<endl;
  }
  return 0;
}