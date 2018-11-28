/*
 * C.cpp
 * Copyright (C) 2015 Chen Ran <crccw@moonux.org>
 *
 * Distributed under terms of the CC-BY-SA 4.0 license.
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <algorithm>
#define INF 0x3f3f3f3f
#define MAXN 100100
#define mp make_pair
#define pb push_back
const double EPS=1e-9;

using namespace std;
typedef long long LL;

int c[5][5]={
  0, 0, 0, 0, 0,
  0, 1, 2, 3, 4,
  0, 2,-1, 4,-3,
  0, 3,-4,-1, 2,
  0, 4, 3,-2,-1
};

int b[9][9],f[9][9];

int con(char c){
  switch(c){
    case '1':return 1;
    case 'i':return 2;
    case 'j':return 3;
    case 'k':return 4;
  }
}

int calc(int lhs, int rhs){
  if(lhs==0) return rhs;
  if(rhs==0) return lhs;
  bool negtive=false;
  if(lhs*rhs<0) negtive=true;
  return (negtive?-1:1)*c[abs(lhs)][abs(rhs)];
}

int main(int argc, char *argv[])
{
  for(int i=-4;i<=4;i++){
    if(i==0) continue;
    for(int j=-4;j<=4;j++){
      if(j==0) continue;
      b[calc(i,j)+4][j+4]=i;
      f[i+4][calc(i,j)+4]=j;
    }
  }
  int t,L,X;
  string s;
  string ts;
  bool ok;
  cin>>t;
  for(int cas=1;cas<=t;cas++){
    cout<<"Case #"<<cas<<": ";
    ok=false;
    cin>>L>>X;
    cin>>s;
    ts="";
    int f1,f2,f3,mid,l,r;
    for(int i=1;i<=X;i++) ts+=s;
    if(X*L<3){
      cout<<"NO"<<endl;
    }else{
      f1=f2=f3=l=mid=0;
      for(int i=0;i<X*L;i++) mid=calc(mid,con(ts[i]));
      while(l<L*X-2){
        while(f1!=2&&l<L*X-2){
          f1=calc(f1,con(ts[l]));
          mid=f[con(ts[l])+4][mid+4];
          l++;
        }
        if(f1!=2) break;
        r=L*X-1;
        f2=mid;f3=0;
        while(l<r){
          while(f3!=4&&l<r){
            f3=calc(con(ts[r]),f3);
            f2=b[f2+4][con(ts[r])+4];
            r--;
          }
          if(f3!=4) break;
          if(f2==3){
            ok=true;
            break;
          }else{
            f3=calc(con(ts[r]),f3);
            f2=f[f2+4][con(ts[r])+4];
            r--;
          }
        }
        if(ok) break;
        f1=calc(f1,con(ts[l]));
        mid=b[con(ts[l])+4][mid+4];
        l++;
      }
      //if(ok){
        //f1=0;
        //for(int i=0;i<l;i++) f1=calc(f1,con(ts[i]));
        //f2=0;
        //for(int i=l;i<=r;i++) f2=calc(f2,con(ts[i]));
        //f3=0;
        //for(int i=r+1;i<L*X;i++) f3=calc(f3,con(ts[i]));
        //if(!(f1==2&&f2==3&&f3==4)) {
         //cout<<"WRONG!!!!("<<l<<" "<<r<<")"; 
        //}
      //}
      if(ok) cout<<"YES"<<endl;
      else cout<<"NO"<<endl;
    }
  }
  return 0;
}
