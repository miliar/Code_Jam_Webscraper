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
typedef unsigned long long ULL;
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



int n, j;

vector<ULL> divisors(11);
int bits[32];

bool f(ULL x, int base){
	ULL orig_x = x;
	FOR(i, n){
		bits[i] = (x & 1);
		x >>= 1;
	}
	assert(!x);
	ULL y = 0;
	for(int i = n - 1; i >= 0; i--){
		y *= base;
		y += bits[i];
	}

	const unsigned short l = (unsigned short)min(100ull, orig_x);
	for(unsigned short i = 2; i < l; i++){
		if(y % i == 0){
			divisors[base] = i;
			return true;
		}
	}

	return false;
}

int main(){
	ifstream be("C-small-attempt0.in");
	ofstream ki("ki.txt"); 
	int T;
	be >> T;
	FOR(tt, T){
		ki << "Case #" << tt + 1 << ": " << endl;
		be >> n >> j;
		ULL x = 1ull << (n - 1);
		ULL L = 1ull << n;
		for(; j; x++){
			if(x >= L){
				cout << "Fail!" << endl;
				system("pause");
				exit(1);
			}
			if((x & 1) == 0)
				continue;
			bool ok = true;
			for(int i = 2; i <= 10; i++){
				ok &= f(x, i);
			}
			if(ok){
				j--;
				for(int i=n-1; i>=0; i--) {
					ki << bits[i];
					cout << bits[i];
				}
				cout << " " << j << endl;
				for(int i = 2; i <= 10; i++)
					ki << " " << divisors[i];
				ki << endl;
			}
		}
	}

	ki.close();
	system("pause");
	return 0;
}