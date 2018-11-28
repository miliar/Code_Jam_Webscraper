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
	string s;
	getline(be, s);
	FOR(tt, T){
		getline(be, s);
		int r = 0;
		FOR(i, SZ(s))
			if(s[i] == '-')
				if(i == 0)
					r++;
				else
					if(s[i - 1] != '-')
						r += 2;
		ki<<"Case #"<<tt+1<<": "<<r<<endl;
	}

	ki.close();
	return 0;
}