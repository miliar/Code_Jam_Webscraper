#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "B"
#define INPUT_SIZE "large" //"small" //  

typedef long double LD;


int in[102][102];
int ot[102][102];

int N, M; 
int maxHeight = 0;
bool process();

int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
		
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
  freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T; 
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
 		// inputs
		scanf("%d%d\n", &N, &M); // remember to put \n
    maxHeight = 0;
    rep(j, N) {
      rep(k, M) {
        int l; scanf("%d", &l);
        if (maxHeight < l) maxHeight = l;
        in[j][k] = l;
      }
    }

    bool bSuccess = process();
    if (bSuccess) printf("Case #%d: YES\n", i + 1);
    else printf("Case #%d: NO\n", i + 1);
	}
	return 0;
}

bool process()
{
  rep(j,N) { rep(k,M) { ot[j][k] = maxHeight; } }
  //bool changed = true;
  while (true) {
    // first match input and output matrices, if same return success
    bool matched = true;
    rep(j,N) { rep(k,M) { if (ot[j][k] != in[j][k]) { matched = false; break; } } if (!matched) break; }
    if (matched) return true;

    //changed = false;
    // now try to find any height less than maxHeight in input
    //int maxX = -1, maxY = -1;
    bool pRow[102];  rep(j,N) { pRow[j] = false; } // processed Row
    
    bool pCol[102];   rep(j,M) { pCol[j] = false; } 
    --maxHeight;
   if (maxHeight > 0) {
       rep(j,N) { 
        rep(k,M) { 
          if (in[j][k] == maxHeight) {
            // check if entire row consists of grass height <= maxHeight
            bool rowFound = true;
            rep(x, M) { if (in[j][x] > maxHeight) { rowFound = false; } }
            if (rowFound && (!pRow[j])) {
              rep(x, M) { ot[j][x] = maxHeight; pRow[j] = true;/*changed = true;*/ } 
            } // entire row found; change output of that row

            // column turn
            bool colFound = true;
            rep(y, N) { if (in[y][k] > maxHeight) { colFound = false; } }
            if (colFound && (!pCol[k])) { 
              rep(y, N) { ot[y][k] = maxHeight; pCol[k] = true; /*changed = true;*/ } 
            } // entire row found; change output of that row

            if (!(rowFound || colFound)) return false;
          } 
        } 
      }

    }

    if (maxHeight <= 0) {return false; }

  }
  // 
  return false;
}
