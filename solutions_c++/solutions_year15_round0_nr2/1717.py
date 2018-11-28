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

int main(){
	ifstream be("B-large.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int d; be >> d;
		VI v;
		FOR(i, d){
			int x; be >> x;
			v.push_back(x);
		}
		VI v_orig(v);
		int mi = 1000000;
		for(int i = 1; i <= 1000; i++){
			v = v_orig;
			int c = 0;
			for(int j = 0; j < SZ(v); j++){
				if(v[j]>i){
					v.push_back(v[j] - i);
					v[j] = i;
					c++;
				}
			}
			mi = min(mi, i + c);
		}
		ki<<"Case #"<<tt+1<<": "<<mi<<endl;
	}

	ki.close();
	return 0;
}