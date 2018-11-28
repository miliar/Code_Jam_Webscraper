#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <cstdio>
#include <functional>

using namespace std;

template<class T>
string tostring(T a){ stringstream ss; ss << a; return ss.str(); }

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> II;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

int main(){
	ifstream be("B-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int n;  be >> n;
		VI xs(n);
		FOR(i, n)
			be >> xs[i];

		const int inf = 10000000;
		int mi = inf;
		for(int mask = 0; mask < (1 << n); mask++){
			int c = 0;
			FOR(i, n){
				for(int j = i + 1; j < n; j++){
					int mi = (mask & (1 << i)) >> i, mj = (mask & (1 << j)) >> j;
					if(mi == 0 && mj == 0){
						if(xs[i] > xs[j]){
							c++;
						}
					} else if(mi == 1 && mj == 1){
						if(xs[i] < xs[j]){
							c++;
						}
					} else if(mi == 0 && mj == 1){
						//semmi
					} else {//(mi == 1 && mj == 0)
						c++;
					}
				}
			}
			if(c < mi){
				mi = c;
			}
		}

		ki << "Case #" << tt + 1 << ": " << mi << endl;
	}


	ki.close();
	return 0;
}