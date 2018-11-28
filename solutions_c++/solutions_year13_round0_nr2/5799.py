#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<queue>
#include<complex>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>

using namespace std;

#define REP(i,a,n) for(int i = a ; i < n ; i++)
#define rep(i,n) REP(i,0,n)

typedef long long ll;

int m[110][110];
int cur[110][110];
int main(){
  int t;
  cin>>t;
  rep(i,t){
    int h,w;
    int mm = 1;
    cin>>h>>w;
    rep(j,h){
      rep(k,w){
        cin>>m[j][k];
        mm = max(mm,m[j][k]);
      }
    }
    
    rep(j,h){
      rep(k,w){
        cur[j][k] = mm;
      }
    }

    rep(ii,10){
      // yoko
      rep(j,h){
        bool f = true;
        rep(k,w){
          if(m[j][k] > m[j][0]){
            f = false;
          }
        }
        if(f){
          rep(k,w){
            cur[j][k] = min(m[j][0],cur[j][k]);
          }
        }
      }
      
      // tate
      rep(j,w){
        bool f = true;
        rep(k,h){
          if(m[k][j] > m[0][j]){
            f = false;
          }
        }
        if(f){
          rep(k,h){
            cur[k][j] = min(m[0][j] , cur[k][j]);
          }
        }
      }
    }
    bool f = true;
    rep(j,h){
      rep(k,w){
        if(m[j][k] != cur[j][k]) f = false;
      }
    }
    
    cout<<"Case #"<<i+1<<": ";
    if(f)cout<<"YES\n";
    else cout<<"NO\n";
  }
}
