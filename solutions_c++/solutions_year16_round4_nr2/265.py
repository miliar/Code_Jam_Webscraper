#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

long double T[500];
int m;

long double f[300][300];

long double calc() {
  f[0][0] = 1;
  for(int i=0;i<m;++i){
    long double x=T[i+1];
    long double y=1-x;
    fill(f[i+1],f[i+1]+i+3,0);
    for(int j=0;j<=i;++j)
      if(f[i][j] > 0) {
        f[i+1][j] += f[i][j] * y;
        f[i+1][j+1] += f[i][j] * x;
      }
  }
  return f[m][m / 2];
}

long double run() {
  long double ans = 0;
  vector<long double> A;
  int N, K;
  cin >> N >> K;
  long double x;
  for(int i=0;i<N;++i){
    cin >> x;
    A.push_back(x);
  }
  sort(A.begin(), A.end());
  for(int a = 0; a <= K; ++ a) {
    int b = K - a;
    m = 0;
    for(int i=0;i<a;++i)T[++m]=A[i];
    for(int i=0;i<b;++i)T[++m]=A[N-1-i];
    ans=max(ans,calc());
  }
  return ans;
}

int main() {
  //freopen("B.in","r",stdin);
  freopen("B-large.in","r",stdin);
  freopen("B.out","w",stdout);
  
  int test;
  cin >> test;
  cout.setf(ios::fixed);
  cout.precision(9);
  for(int no=1;no<=test;++no){
    cout << "Case #"<<no<<": "<<run() << endl;
  }
}
