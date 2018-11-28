#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;
#define REP(i,n) for(int _n=n, i=0;i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define PB push_back

int N;
int A[2222],B[2222];
int tA[2222],tB[2222];
int rst[2222];

void play() {
  memset(rst,-1,sizeof(rst));
  REP(z,N) tA[z]=tB[z]=1;
  FOR(z,1,N) {
    int f = -1;
    for(int i=N-1;i>=0;i--) {
      if (rst[i]<0 && A[i]==tA[i] && B[i]==tB[i]) {
        if (f<0 || (A[i]<A[f] || B[i]<B[f]))
          f=i;
      }
    }
    if (f==-1) {
      cout<<"ooops"<<" "<<z<<endl;
      exit(1);
    }
    // cout<<f<<" "<<z<<" "<<A[f]<<" "<<B[f]<<endl;
    rst[f]=z;
    for (int i=f+1;i<N;i++) if(tA[i]<A[f]+1) tA[i]=A[f]+1;
    for (int i=0;i<f;i++) if(tB[i]<B[f]+1) tB[i]=B[f]+1;
    // REP(i,N) cout<<tA[i]<<" "<<tB[i]<<" - "<<A[i]<<" "<<B[i]<<endl;
  }
}

int main() {
  int Ts;
  cin>>Ts;
  FOR(cs, 1, Ts) {
    cin>>N;
    REP(i,N) cin>>A[i];
    REP(i,N) cin>>B[i];
    play();
    cout << "Case #" << cs << ":";
    REP(i,N) cout<<" "<<rst[i];
    cout<<endl;
  }
  return 0;
}
