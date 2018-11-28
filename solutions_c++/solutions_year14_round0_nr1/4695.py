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


vector<bool> rr(int a, ifstream &be){
	vector<bool> r(16);
	FOR(i,4)
		FOR(j, 4){
			int x; be >> x; x--;
			if(a == i)
				r[x] = true;
		}
	return r;
}

int main(){
	ifstream be("A-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int a1; be >> a1; a1--;
		auto s1 = rr(a1, be);

		int a2; be >> a2; a2--;
		auto s2 = rr(a2, be);

		VI r;
		FOR(i, 16)
			if(s1[i] && s2[i])
				r.push_back(i);
		string ans;
		if(SZ(r) == 0)
			ans = "Volunteer cheated!";
		else if(SZ(r) > 1)
			ans = "Bad magician!";
		else
			ans = tostring(r[0] + 1);

		ki << "Case #" << tt + 1 << ": " << ans << endl;
	}


	ki.close();
	return 0;
}