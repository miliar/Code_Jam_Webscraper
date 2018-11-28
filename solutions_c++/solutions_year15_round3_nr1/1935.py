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
#include <cassert>
#include <array>

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

using mask = unsigned int;

mask set1(int i, mask m){
	return m | (1 << i);
}
mask set0(int i, mask m){
	return m & ~(1 << i);
}
bool get(int i, mask m){
	return m & (1 << i);
}

int R, C, W;

VVI mem;
int f(mask S, mask Q) {
	if(mem[S][Q] == -1) {

		int pc = __popcnt(S);
		if(pc == 1){
			int c = 0;
			FOR(i, C){
				if(get(i, S)){
					assert(i <= C - W);
					for(int j = i; j < i + W; j++){
						if(!get(j, Q)){
							c++;
						}
					}
					break;
				}
			}
			return c;
		}
		if(pc == 0){
			return -100;
		}

		int mi = 1000;
		FOR(i, C){
			/*bool mehet = false;
			for(int j = max(0, i - W + 1); j <= i; j++){
				if(get(j, S)) {
					mehet = true;
					break;
				}
			}*/
			bool mehet = true;
			if(mehet){
				mask m;
				//brother says yes
				m = 0;
				for(int j = max(0, i - W + 1); j <= i; j++){
					m = set1(j, m);
				}
				if((S & m) == S)
					continue;
				int yes = f(S & m, set1(i, Q));
				
				//brother says no
				m = S;
				for(int j = max(0, i - W + 1); j <= i; j++){
					m = set0(j, m);
				}
				if(m == S)
					continue;
				int no = f(m, set1(i, Q));

				int bopt = max(yes, no) + 1;
				if(bopt < mi){
					mi = bopt;
				}
			}
		}
		mem[S][Q] = mi;
	}
	return mem[S][Q];
}

int main(){
	//ifstream be("A-small-attempt0.in");
	ifstream be("A-small-attempt2.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		be >> R >> C >> W;
		assert(R == 1);
		mem = VVI(1 << C, VI(1 << C, -1));
		mask m = 0;
		for(int i = 0; i <= C - W; i++){
			m = set1(i, m);
		}
		int r = f(m, 0);
		assert(r >= W);
		ki << "Case #" << tt + 1 << ": " << r << endl;
	}

	ki.close();
	return 0;
}