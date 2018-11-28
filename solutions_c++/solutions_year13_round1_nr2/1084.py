#include <string.h>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())

#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)
#define ZERO(arr) for(int CNT=0;CNT<sizeof(arr);CNT++){arr[CNT]=0;}

const int MAX = 1000000;
const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int move[4][2] = { {0, 1} , {1, 0} , {0, -1} , {-1, 0} };

//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
int ans;

uint32_t my32;
uint64_t modArr[3][3];

uint64_t v[10001];
uint64_t maxV[10001][6];

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  ifstream inFile(argv[1]);
  ofstream outFile("output.txt", fstream::trunc);

  inFile >> nCases;
  cout << nCases << " cases." << endl;
  for0n(c,nCases) {
    int E, R, N;
    inFile >> E >> R >> N;

    for0n(i, N) {
      inFile >> v[i];
    }
    N--;
    if (R>E) {
      R=E;
    }

    for(j = R; j <= E; j++) {
      maxV[N][j] = v[N] * j;
      // cout << "max " << N << " " << j << "= " << maxV[N][j] << endl;
    }

    for(i = N - 1; i >= 0; i--) {
      for(j = R; j <= E; j++) {
        uint64_t localMax = 0;
        for(k = 0; k <= j; k++) {
          uint64_t canGet = (k*v[i]) + maxV[i+1][min(j - k + R, E)];
          // cout << "canGet " << i << " " << j << ":" << k << "= " << canGet << endl;

          localMax = max(localMax, (k*v[i]) + maxV[i+1][min(j - k + R, E)]);
          // cout << "lmax " << i << " " << j << "= " << localMax << endl;
        }
        maxV[i][j] = localMax;
        // cout << "maxV " << i << " " << j << "= " << localMax << endl;
      }
    }

    ans = maxV[0][E];

    cout << "Case #" << c + 1 << ": " << ans << endl;
    outFile << "Case #" << c + 1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
