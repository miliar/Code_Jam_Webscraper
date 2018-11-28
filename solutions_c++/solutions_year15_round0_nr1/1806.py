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
		int n; be >> n;
		string s; be >> s;
		assert(SZ(s) == n + 1);
		int sum = 0;
		int r = 0;
		FOR(i, n + 1){
			if(sum < i){
				r += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		ki << "Case #" << tt + 1 << ": " << r << endl;
	}


	ki.close();
	return 0;
}