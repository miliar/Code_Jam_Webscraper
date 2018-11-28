#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define repn(i,m,n) for(int i=m;i<n;i++)
using namespace std;
int fun(vector<int> &s,int av){
  int t=0;
  rep(i,s.size()){
    t+=abs(av-s[i]);
  }
  return t;
}
bool initTT(vector<vector<int> > &tt,vector<string> &ss,string &p,int N){
  rep(i,N){
    int cnt=1;
    char c=ss[i][0];
    if(c==0) {
      if(p.length()>0) return false;
    }

    for(int j=1;;j++){
      if(c==ss[i][j]){cnt++;}
      else{
        //size not ..
        if(p.length()<=tt[i].size()||c!=p[tt[i].size()])  return false;
        tt[i].push_back(cnt);
        cnt=1;
        c=ss[i][j];
      }
      if(ss[i][j]==0) {
        if(tt[i].size()!=p.length()) return false;
        break;
      }
    }
  }
  return true;
}
int getN(vector<vector<int> > &tt,string &p,int N){
  int res=0;
    // rep(i,N) {
      // rep(j,p.length())
      // cout<<tt[i][j]<<" ";cout<<endl;
    // }
  vector<int> num;
  rep(j,p.length()){
    num.clear();
    num.push_back(0);
    repn(i,1,N){
      int tmp=0;
        num.push_back(tt[i][j]-tt[0][j]);
        // if(j>0&&tt[i][j]!=tt[i][j-1]) { return -1;}
      }
    // rep(i,N) cout<<num[i]<<" ";cout<<endl;
    int total=0;
    rep(i,num.size()){total+=num[i];}
    int av=total/N;
    int Num=min(fun(num,av-1),fun(num,av));
    Num=min(Num,fun(num,av+1));
    res+=Num;
  }
  return res;
}



int main(){
  int cases;cin>>cases;
  for(int caseI=1;caseI<=cases;caseI++){
    int Num=0; 
    bool flag=true;
    int N;cin>>N;
    vector<string> ss;
    string s;
    rep(i,N){cin>>s;ss.push_back(s);}
    if(N>1) {
      string p;
      vector<int> t;
      char c=0;
      for(int i=0;;i++){
        if(ss[0][i]!=c){
          if(ss[0][i]!=0) p+=(ss[0][i]);
          c=ss[0][i];
        }
        if(ss[0][i]==0) break;
      }
      // cout<<"p:"<<p<<endl;

      vector<vector<int> > tt(N);
      if(!initTT(tt,ss,p,N)) {flag=false;}
      if(p.length()>0) {
        if(flag) {Num=getN(tt,p,N);}
      }
    }
    if(!flag||Num<0){ printf("Case #%d: Fegla Won\n",caseI);}
    else { printf("Case #%d: %d\n",caseI,Num);}
  }
  return 0;
}

