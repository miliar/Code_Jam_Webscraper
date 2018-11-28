#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define F first
#define S second
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)(x).size())
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) {
  return s<<"("<<p.first<<","<<p.second<<")";
}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ ";
  for (auto it : c) s << it << " ";
  s<<"]";
  return s;
}
// Let's Fight!

const int MAXN = 205;

int N, K;
double arr[MAXN];
double dp[MAXN], tmp[MAXN];

double calc_prob(vector<double> vec)
{
  FZ(dp);
  dp[0] = 1;
  for(auto x: vec)
  {
    FZ(tmp);
    for(int i=0; i<=N; i++)
    {
      tmp[i] += dp[i] * (1-x);
      if(i < N) tmp[i+1] += dp[i] * x;
    }
    swap(dp, tmp);
  }

  return dp[K/2];
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N>>K;
    for(int i=0; i<N; i++)
      cin>>arr[i];
    sort(arr, arr+N);
    double ans = 0;
    for(int i=0; i<=K; i++)
    {
      vector<double> vec;
      for(int j=0; j<i; j++)
        vec.PB(arr[j]);
      for(int j=0; j<K-i; j++)
        vec.PB(arr[N-1-j]);
      double p = calc_prob(vec);
      ans = max(ans, p);
    }
    cout<<"Case #"<<t<<": "<<fixed<<setprecision(10)<<ans<<endl;
  }

  return 0;
}
