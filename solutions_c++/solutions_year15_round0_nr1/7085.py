#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define MP make_pair
#define F first
#define S second
#define SZ(x) x.size()

#define PB push_back
#define EB emplace_back

#define DEBUG(x) cout << #x << " = "; cout<<x<<endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout<<a[_]<<' ';cout<<endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout<<a[_]<<' ';cout<<endl;

const double PI = acos(-1.0);
const double EPS = 1e-10;

typedef long long i64;
typedef unsigned long long ui64;
typedef vector<int> vi;
typedef pair<int,int> pii;

int nTestCases,nMaxShyness;
int prefixSum[1005];
string shynessLevel;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin>>nTestCases;
  REP(t,nTestCases) {
    cin>>nMaxShyness>>shynessLevel;
    REP(i,SZ(shynessLevel)) {
      int curDigit=shynessLevel[i]-'0';
      if(i>=1) prefixSum[i]=prefixSum[i-1]+curDigit;
      else prefixSum[i]=curDigit;
    }
    int nAdditionalInvite = 0;
    FOR(i,1,SZ(shynessLevel)-1) {
      if(prefixSum[i-1]<i) {
        int f = i-prefixSum[i-1];
        int curDigit=shynessLevel[i]-'0';
        nAdditionalInvite+=f;
        REP(i,SZ(shynessLevel))
          prefixSum[i]+=f;
      }
    }
    cout<<"Case #"<<t+1<<": "<<nAdditionalInvite<<endl;
  }
  return 0;
}
