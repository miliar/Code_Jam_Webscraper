//Program: d
//Author: gary
//Date: 12/04/2014
#include <bits/stdc++.h>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef pair<int, int> i2;
typedef long long ll;
const int INF = 1e9;
const int MAX_N = 1000 + 1;
// #define DEBUG
int N;
double f[MAX_N];
double g[MAX_N];
double tt[MAX_N * 2];

int simulate(deque<int> A, set<int> B)
{
  int points = 0;
  for(auto a: A)
  {
    auto b = B.lower_bound(a);
    if(b == B.end())
    {
      points ++;
      B.erase(B.begin());
    }
    else
    {
      B.erase(b);
    }
  }
  return points;
}

int simulate2(deque<int> A, deque<int> B)
{
  int points = 0;
  for(int i = 0; i < SZ(A); i++)
    points += A[i] > B[i];
  return points;
}

void print(vector<int> s)
{
  for(int a: s)
  {
    printf("%d ", a);
  }
  puts("");
}

void print(deque<int> s)
{
  for(int a: s)
  {
    printf("%d ", a);
  }
  puts("");
}

void print(set<int> s)
{
  for(int a: s)
  {
    printf("%d ", a);
  }
  puts("");
}

int main(){
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++)
  {
    cin >> N;
    for(int i = 0; i < N; i++) cin >> f[i], tt[i] = f[i];
    for(int i = 0; i < N; i++) cin >> g[i], tt[i + N] = g[i];
    sort(tt, tt + 2 * N);

    deque<int> A, B;

    for(int i = 0; i < N; i++)
    {
      A.pb(lower_bound(tt, tt + 2 * N, f[i]) - tt);
      B.pb(lower_bound(tt, tt + 2 * N, g[i]) - tt);
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

#ifdef DEBUG
    print(A);
    print(B);
#endif

    int ans1 = 0;
    int ans2 = simulate(A, set<int>(B.begin(), B.end()));
    
    for(int i = 0; i < N; i++)
    {
      ans1 = max(ans1, simulate2(A, B));
#ifdef DEBUG
      printf("i = %d\n", i);
      print(A);
      print(B);
#endif
      A.pop_front();
      B.pop_back();

    }
    printf("Case #%d: %d %d\n", tc, ans1, ans2);
  }
  return 0;
}
