#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
int h[100][100];
int max_row[100], max_column[100];
int main() {
  int T;
  cin>>T;
  REP(tt,T) {
    bool ans=true;
    int m,n;
    cin>>n>>m;
    REP(i,n)  {
      REP(j,m) {
        cin>>h[i][j];
      }
    }
    REP(i,n) {
      max_row[i]=h[i][0];
      REP(j,m) max_row[i]=max(max_row[i], h[i][j]);
    }
    REP(j,m) {
      max_column[j]=h[0][j];
      REP(i,n) max_column[j]=max(max_column[j], h[i][j]);
    }
    REP(i,n) REP(j,m) {
      if(h[i][j]<max_row[i] && h[i][j]<max_column[j]) ans=false;
    }
    
    cout<<"Case #"<<(1+tt)<<": "<<(ans?"YES":"NO")<<endl;
  }  
}
// issue choosing small type
