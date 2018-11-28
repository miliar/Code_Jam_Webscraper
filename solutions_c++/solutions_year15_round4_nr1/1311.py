#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<iostream>
#include<vector>
#define REP(i,n) for(int (i)=0;i<(int)(n);++i)

using namespace std;
int dx[4]={  0,  1,  0,  -1};
int dy[4]={  1,  0,  -1,  0};
char c[4]={  'v','>','^','<' };
void solve() {
int n,m;
cin>>n>>m;
vector<string> s(n);
REP(i,n) cin>>s[i];
int rval=0;
int ok=1;
REP(i,n) REP(j,m) if(s[i][j]!='.') {
  int in[4]={0,0,0,0};
 REP(d,4) {
   int x=j+dx[d];
   int y=i+dy[d];
   while(1) {
     if(x<0 || y<0 || x>=m || y>=n) {
       break;
     }
     if(s[y][x]!='.') {
       in[d]=1;
       break;
     }
     x+=dx[d];
     y+=dy[d];
   } 
 }
 int some=0;
 REP(d,4) {
   some|=in[d];
   if(c[d]==s[i][j] && !in[d])rval++; 
 }
 if(!some) {
   ok=0;
 }

}


if(!ok) cout<<"IMPOSSIBLE"<<endl;else
cout<<rval<<endl;
}
int main() {
int T;cin>>T;REP(i,T) {
cout<<"Case #"<<(i+1)<<": ";
solve();
}
}
