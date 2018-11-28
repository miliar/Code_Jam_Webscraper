#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
using namespace std;

#define rep(i,m,n) for(int i = m; i < n; i++)
#define bitrep(S, m, n) for(int S = m; S < (1 << n); S++)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define x first
#define y second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int, int> PII;

int fstcard[16], seccard[16];

int main(){
  int loop, fstans, secans;
  ifstream ifs("A-small-attempt1.in");
  ofstream ofs("ans.text");
  ifs >> loop;
  rep(l, 1, loop+1){
    ifs >> fstans;
    rep(i, 0, 16) ifs >> fstcard[i];
    ifs >> secans;
    rep(i, 0, 16) ifs >> seccard[i];
    int count = 0, ans;
    rep(i, 0, 4){
      rep(j, 0, 4){
	if(fstcard[(fstans-1)*4+i] == seccard[(secans-1)*4+j]){
	  count++;
	  ans = fstcard[(fstans-1)*4+i];
	}
      }
    }
    if(count == 0) ofs << "Case #" << l << ": Volunteer cheated!";
    else if(count == 1) ofs << "Case #" << l << ": " << ans;
    else ofs << "Case #" << l << ": Bad magician!";
    ofs << endl;
  }
  return 0;
}
