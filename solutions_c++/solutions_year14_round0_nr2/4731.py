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
#include <iomanip>

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
		double c, f, x; be >> c >> f >> x;
		double prev_r = numeric_limits<double>::max();
		double t = 0;
		double s = 2;
		while(1){
			double r = t + x / s;
			//cout << r << endl;
			if(r > prev_r)
				break;
			prev_r = r;
			t += c / s;
			s += f;
		}
		ki << setprecision(20) << "Case #" << tt + 1 << ": " << prev_r << endl;
		//cout << endl;
	}


	ki.close();
	return 0;
}