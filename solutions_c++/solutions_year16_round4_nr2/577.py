#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#define LL long long int
using namespace std;

int N,K;
vector<double> P;

void read()
{
  P.clear();
  cin >> N >> K;
  for(int i=0;i<N;i++)
    {
      double t;
      cin >> t;
      P.push_back(t);
    }
  sort(P.begin(),P.end());
}

double solve(vector<double> X)
{
  double V[K+1];
  for(int i=0;i<=K;i++)
    V[i]=0;
  V[0]=1;
  for(int i=0;i<K;i++)
    {
      double V1[K+1];
      for(int j=0;j<=K;j++)
	V1[j]=V[j]*(1-X[i]);
      for(int j=1;j<=K;j++)
	V1[j]+=V[j-1]*X[i];
      for(int i=0;i<=K;i++)
	V[i]=V1[i];
    }
  return V[K/2];
}

vector<double> get(int k)
{
  vector<double> rst;
  for(int i=0;i<k;i++)
    rst.push_back(P[i]);
  for(int j=1;j<=K-k;j++)
    rst.push_back(P[N-j]);
  return rst;
}

double solve()
{
  double max = 0;
  for(int k=0;k<=K;k++)
    {
      double p = solve(get(k));
      if(max<p)
	max=p;
    }
  return max;
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #" << t << ": ";
      printf("%.6lf",solve());
      cout << endl;
    }
  return 0;
}
