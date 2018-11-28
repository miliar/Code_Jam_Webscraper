#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

int N;
int grille[4][4];
int tmp[4][4];
bool taken[4];
bool here[4];

bool bourrin()
{
  for (int i=0; i<N; i++)
  if (here[i])
  {
    here[i] = false;
    
    bool ok = false;
    for (int j=0; j<N; j++)
      if (!taken[j] && tmp[i][j])
        ok = true;
    if (!ok) return false;
    
    for (int j=0; j<N; j++)
    if (!taken[j] && tmp[i][j])
    {
      taken[j] = true;
      if (!bourrin())
        return false;
      taken[j] = false;
    }
    
    here[i] = true;
  }
  
  return true;
}

bool check()
{
  for (int i=0; i<N; i++)
  {
    here[i] = 1;
    taken[i] = 0;
  }
  
  return bourrin();
}

void main2()
{
  cin >> N;
  for (int i=0; i<N; i++)
  {
    string s;
    cin >> s;
    for (int j=0; j<N; j++)
      grille[i][j] = (s[j] == '1');
  }
  
  int best = N*N;
  for (int mask=0; mask<(1<<(N*N)); mask++)
  {
    int cost = 0;
    bool ok = true;
    for (int i=0; i<N*N; i++)
    {
      tmp[i/N][i%N] = (mask & (1 << i)) ? 1 : 0;
      if (tmp[i/N][i%N] && !grille[i/N][i%N])
        cost++;
      if (!tmp[i/N][i%N] && grille[i/N][i%N])
        ok = false;
    }
    if (!ok) continue;
    if (check())
      best = min(best, cost);
  }
  
  cout << best << endl;
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
