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
	ifstream be("A-large.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int n;
		be >> n;

		if(n == 0){
			ki << "Case #" << tt + 1 << ": " << "INSOMNIA" << endl;
		} else {
			vector<char> v(10);
			int num_seen = 0;
			int last_seen = n;
			int x = n;
			while(num_seen < 10){
				for(int y = x; y; y /= 10){
					int d = y % 10;
					if(!v[d]){
						num_seen++;
						v[d] = true;
					}
				}
				last_seen = x;
				x += n;
			}
			ki << "Case #" << tt + 1 << ": " << last_seen << endl;
		}
	}

	ki.close();
	return 0;
}