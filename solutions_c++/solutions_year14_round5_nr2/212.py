#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iomanip>
#include <map>

using namespace std;

typedef long long ll;

int P, Q, N;
vector<int> H, G;

void read()
{
  cin >> P >> Q >> N;
  H.resize(N);
  G.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> H[i] >> G[i];
  }
}

int DP[100][201][2000][2];
ll states = 0;

int f(int monster, int hp, int shots, bool myturn)
{
  if (monster == N) return 0;

  int &res = DP[monster][hp][shots][myturn];
  if (res >= 0) return res;



  states++;
  //  if (states % 10000 == 0) cerr << "states = " << states << endl;
  int gold = 0;
  if (shots > 0 && myturn) {
    int hp2 = max(hp - P, 0);
    int monster2 = monster;
    if (hp2 == 0) {
      gold = G[monster];
      monster2++;
      if (monster2 < N) 
	hp2 = H[monster2];
    }
    res = max(res, gold + f(monster2, hp2, shots-1, shots > 0));
  }

  // decide to skip, or forced to skip
  int hp2 = !myturn ? max(hp - Q, 0) : hp;
  int monster2 = monster;
  if (hp2 == 0) {
    monster2++;
    if (monster2 < N)
      hp2 = H[monster2];
  }
  res = max(res, f(monster2, hp2, shots + (!myturn), !myturn));

  //  cout << "f(" << monster << ", " << hp << ", " << shots << ", " << myturn << ") = " << res << endl;
  
  return res;
}


void solve()
{
  read();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j <= 10*N; j++) {
      for (int k = 0; k <= 200; k++) {
	for (int m = 0; m < 2; m++) {
	  DP[i][k][j][m] = -1;
	}
      }
    }
  }

  cout << f(0, H[0], 1, true) << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
