#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair
#define sqr(a) ((a) * (a))

using namespace std;

const int MaxN = 30;

struct TTacka{
  double x, y, u;
  int i;

  TTacka(){
  }

  TTacka(double _x , double _y, int _i){
    x = _x;
    y = _y;
    i = _i;
  }


  friend bool operator < (const TTacka& a , const TTacka& b){
		if (fabs(a.u - b.u) < 1e-9)
			return sqrt(sqr(a.x) + sqr(a.y)) < sqrt(sqr(b.x) + sqr(b.y));
    return a.u < b.u;
  }
};

vector<TTacka> T;

int lambda(double x1, double y1, double x2, double y2, double p, double q){
  double l = p * (y2 - y1) + q * (x1 - x2) + y1 * x2 - y2 * x1;
  if (fabs(l) < 1e-9)
  	return 0;
 	else if (l > 0)
 		return 1;
  else
  	return -1;
}

int next[MaxN], prev[MaxN];

int Eliminate() {
  int N = T.sz;
  double xsr = 0.0, ysr = 0.0;
  for (int i = 0 ; i < N ; i++){
  	xsr += T[i].x;
  	ysr += T[i].y;
 	}

 	xsr /= (double)(N);
 	ysr /= (double)(N);

  for (int i = 0 ; i < N ; i++)
  	T[i].u = atan2(T[i].x - xsr , T[i].y - ysr);

  sort(all(T));

  // Make a double linked list.
  next[0] = 1;
  prev[0] = N - 1;
  next[N - 1] = 0;
  prev[N - 1] = N - 2;
  for (int i = 1 ; i < (N - 1) ; i++){
  	next[i] = i + 1;
  	prev[i] = i - 1;
 	}
 	
  int idx = 0;
  for (int i = 0 ; i < N ; i++)
  	if (T[i].x < T[idx].x)
  	  idx = i;
 		else if (fabs(T[i].x - T[idx].x) < 1e-9 && T[i].y < T[idx].y)
  	  idx = i;

 	int i = idx;
  while (next[i] != idx){
		int lam = lambda(T[i].x , T[i].y , T[next[next[i]]].x , T[next[next[i]]].y , T[next[i]].x , T[next[i]].y);
    if (lam > 0){
      next[i] = next[next[i]];
      prev[next[i]] = i;
      N--;
      if (i != idx)
     		i = prev[i];
    }
    else
    	i = next[i];
  }
  
  return idx;
}


int main(){
  freopen("Cs.out","wt", stdout);
  freopen("Cs.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int n;
    cin >> n;
    int ret[n];
    FOR (i, n)
      ret[i] = 12345;
    int x[n], y[n];
    FOR (i, n)
      cin >> x[i] >> y[i];
    ffor (mask, 1, 1 << n) {
      T.clear();
      int cc = 0;
      map<int, int> mapa;
      FOR (i, n)
        if (mask & (1 << i)) {
          mapa[cc] = i;
          T.pb(TTacka(x[i], y[i], cc));
          cc++;
        }
      int idx = Eliminate();
      int i = idx;
      do {
        int id = mapa[T[i].i];
        ret[id] = min(ret[id], n - cc);
        i = next[i];
        // cout << id << " " << x[id] << " " << y[id] << endl;
      } while (i != idx);
    }
    cout << "Case #" << (test + 1) << ": ";
    cout << "\n";
    FOR (i, n)
      cout << ret[i] << endl;
  }
  return 0;
}
