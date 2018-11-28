#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

#define INF 10000000000000009LL

#define NMAX 1000000

int LeftUpMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = 0;c1<c;c1++)if(VS[r][c1]!='.') ret = 0;
  for(int r1 = 0;r1<r;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}
int RightUpMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = c+1;c1<C;c1++)if(VS[r][c1]!='.') ret = 0;
  for(int r1 = 0;r1<r;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}
int LeftDownMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = 0;c1<c;c1++)if(VS[r][c1]!='.') ret = 0;
  for(int r1 = r+1;r1<R;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}
int RightDownMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = c+1;c1<C;c1++)if(VS[r][c1]!='.') ret = 0;
  for(int r1 = r+1;r1<R;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}

int LeftMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = 0;c1<c;c1++)if(VS[r][c1]!='.') ret = 0;
  return ret;
}
int RightMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int c1 = c+1;c1<C;c1++)if(VS[r][c1]!='.') ret = 0;
  return ret;
}
int DownMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int r1 = r+1;r1<R;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}
int UpMost(int r, int c, int R, int C, vector<string> &VS)
{
  int ret = 1;
  for(int r1 = 0;r1<r;r1++)if(VS[r1][c]!='.') ret = 0;
  return ret;
}

int main(void)
{
  int T,t;
  ll ret;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int R, C;
    cin>>R>>C;
    vector<string> VS;
    int ans = 0;
    int imp = 0;
    int r,c;
    for(r=0;r<R;r++){
      string s;
      cin>>s;
      VS.PB(s);
    }
    if(C==1&&R==1) {
      r=0;
      c=0;
      if(VS[r][c] != '.')imp = 1;
    }
    else if(C==1) {
      //imp判定
      c = 0;
      int cnt = 0;
      for(r=0;r<R;r++){
        if(VS[r][c]!='.')cnt++;
      }
      if(cnt == 1){
        imp = 1;
      }
      cnt = 0;
      char last = '.';
      for(r=0;r<R;r++){
        if(VS[r][c]=='.')continue;
        cnt++;
        if(cnt == 1 ){
          if(VS[r][c] != 'v')ans++;
        }
        else {
          if(VS[r][c] == '<' || VS[r][c] == '>' )ans++;
          last = VS[r][c];
        }
      }
      if(last == 'v')ans++;
    }
    else if(R==1) {
      //imp判定
      r = 0;
      int cnt = 0;
      for(c=0;c<C;c++){
        if(VS[r][c]!='.')cnt++;
      }
      if(cnt == 1){
        imp = 1;
      }
      cnt = 0;
      char last = '.';
      for(c=0;c<C;c++){
        if(VS[r][c]=='.')continue;
        cnt++;
        if(cnt == 1 ){
          if(VS[r][c] != '>')ans++;
        }
        else {
          if(VS[r][c] == 'v' || VS[r][c] == '^' )ans++;
          last = VS[r][c];
        }
      }
      if(last == '>')ans++;
    }
    else  {
      //imp判定
      for(r=0;r<R;r++){
        for(c=0;c<C;c++){
          if(VS[r][c]!='.'){
            int cnt2=0;
            for(int c1=0;c1<C;c1++){
              if(c==c1)continue;
              if(VS[r][c1]!='.')cnt2++;
            }
            for(int r1=0;r1<R;r1++){
              if(r==r1)continue;
              if(VS[r1][c]!='.')cnt2++;
            }
            if(cnt2==0)imp=1;
          }
        }
      }
      for(r=0;r<R;r++){
        for(c=0;c<C;c++){
          int cnt = 0;
          if(VS[r][c]=='.')continue;
          //左上
          if(LeftUpMost(r,c,R,C,VS)==1){
            //右にいない
            if(RightUpMost(r,c,R,C,VS)==1){
              if(VS[r][c] != 'v')ans++;
            }
            //下にいない
            else if(LeftDownMost(r,c,R,C,VS)==1){
              if(VS[r][c] != '>')ans++;
            }
            //右もしたもいる
            else {
              if(VS[r][c] == '<' || VS[r][c] == '^')ans++;
            }
          }
          //右上
          else if(RightUpMost(r,c,R,C,VS)==1){
            //下にいない
            if(RightDownMost(r,c,R,C,VS)==1){
              if(VS[r][c] != '<')ans++;
            }
            //下にいる
            else {
              if(VS[r][c] == '>' || VS[r][c] == '^')ans++;
            }
          }
          //左下
          else if(LeftDownMost(r,c,R,C,VS)==1){
            //右にいない
            if(RightDownMost(r,c,R,C,VS)==1){
              if(VS[r][c] != '^')ans++;
            }
            else{
              //上と右はいる
              if(VS[r][c] == '<' || VS[r][c] == 'v')ans++;
            }
          }
          //右下
          else if(RightDownMost(r,c,R,C,VS)==1){
            //上にいない
            if(RightUpMost(r,c,R,C,VS)==1){
              if(VS[r][c] != '<')ans++;
            }
            //上と左はいる
            if(VS[r][c] == '>' || VS[r][c] == 'v')ans++;
          }
          //左
          else if(LeftMost(r,c,R,C,VS)==1){
            if(RightMost(r,c,R,C,VS)==1){
              if(VS[r][c] == '<' ||(VS[r][c] == '>'))ans++;
            }
            else
              if(VS[r][c] == '<')ans++;
          }
          //右
          else if(RightMost(r,c,R,C,VS)==1){
            if(VS[r][c] == '>')ans++;
          }
          //上
          else if(UpMost(r,c,R,C,VS)==1){
            if(DownMost(r,c,R,C,VS)==1){
              if(VS[r][c] == 'v' || VS[r][c] == '^')ans++;
            }
            else
              if(VS[r][c] == '^')ans++;
          }
          //下
          else if(DownMost(r,c,R,C,VS)==1){
            if(VS[r][c] == 'v')ans++;
          }
        }
      }
    }
    if(imp==1)
      cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
    else
      cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}

