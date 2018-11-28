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
	ifstream be("A-large.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int n, cap;  be >> n >> cap;
		VI fs;
		FOR(i, n){
			int x;  be >> x;
			fs.push_back(x);
		}
		sort(ALL(fs));
		vector<bool> b(n, true);

		int sol = 0;
		for(int i = n - 1; i >= 0; i--){
			if(b[i]){
				b[i] = false;
				int fr = cap - fs[i];
				int j = upper_bound(ALL(fs), fr) - fs.begin();
				j--;
				while(j >= 0 && (!b[j] || fs[j] > fr))
					j--;
				if(j>=0)
					b[j] = false;
				sol++;
			}
		}

		ki << "Case #" << tt + 1 << ": " << sol << endl;
	}


	ki.close();
	return 0;
}