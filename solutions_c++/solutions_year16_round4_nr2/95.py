#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

double p[200];
double dyn[201][101];

double proba(vi v)
{
  int half = v.size()/2;
  for (int i=0; i<v.size(); i++)
    dyn[0][i] = 0;
  dyn[0][0] = 1;
  
  for (int i=0; i<v.size(); i++)
  {
    for (int j=0; j<=half; j++)
    {
      dyn[i+1][j] = (1 - p[v[i]]) * dyn[i][j];
      if (j > 0) dyn[i+1][j] += p[v[i]] * dyn[i][j-1];
    }
  }
  
  return dyn[v.size()][half];
}

void main2()
{
  int N, K;
  cin >> N >> K;
  for (int i=0; i<N; i++)
    cin >> p[i];
  
  double best = 0;
  
  /*
  int set = (1 << K) - 1;
  while (set < (1<<N))
  {
    vi act;
    for(int j=0;j<N;++j)
      if((set>>j)&1)
        act.push_back(j);
    
    best = max(best, proba(act));
    
    int c = set & -set;
    int r = set + c;
    set = (((r^set) >> 2) / c) | r;
  }
  */
  
  sort(p, p+N);
  
  for (int i=0; i<=K; i++)
  {
    vi act;
    for (int j=0; j<i; j++)
      act.push_back(j);
    for (int j=0; j<K-i; j++)
      act.push_back(N-1-j);
    
    best = max(best, proba(act));
  }
  
  cout << fixed << setprecision(9) << best << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
