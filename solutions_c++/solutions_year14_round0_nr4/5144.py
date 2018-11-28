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
#include <iomanip>
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

double naomi[10], ken[10];
bool used[10];

int main(){
  int loop;
  ifstream ifs("D-small-attempt0.in");
  
  ofstream ofs("ans.txt");
  ifs >> loop;
  int N;
  rep(l, 1, loop+1){
    ifs >> N;
    rep(i, 0, N) ifs >> naomi[i];
    rep(i, 0, N) ifs >> ken[i];
    memset(used, false, sizeof(used));
    
    double diff;
    int index, ansf = 0, anss = 0;
    rep(i, 0, N){
      diff = 3;
      index = 11;
      rep(j, 0, N){
	if(ken[i] < naomi[j] && naomi[j] - ken[i] < diff && !(used[j])){ 
	  diff = naomi[j] - ken[i];
	  index = j;
	}
      }
      if(index < N){
	used[index] = true;
	ansf++;
      }
    }
    
    memset(used, false, sizeof(used));
    rep(i, 0, N){
      diff = 3;
      index = 11;
      rep(j, 0, N){
	if(naomi[i] < ken[j] && ken[j] - naomi[i] < diff && !used[j]){ 
	  diff = ken[j] - naomi[i];
	  index = j;
	}
      }
      if(index < N){
	used[index] = true;
	anss++;
      }
    }
    
    ofs << "Case #" << l << ": " << ansf << " " << N - anss;
    ofs << endl;
  }
  return 0;
}
