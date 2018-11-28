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

// R -> S
// S -> P
// P -> R
// RSP
char winner(char a, char b){
	if(a == 'R' && b == 'S') return 'R';
	if(a == 'R' && b == 'P') return 'P';
	if(a == 'S' && b == 'R') return 'R';
	if(a == 'S' && b == 'P') return 'S';
	if(a == 'P' && b == 'R') return 'P';
	if(a == 'P' && b == 'S') return 'S';
}

int main(){
	ifstream be("A-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int n, r, p, s;
		be >> n >> r >> p >> s;

		vector<char> v;
		FOR(i, p)
			v.push_back('P');
		FOR(i, r)
			v.push_back('R');
		FOR(i, s)
			v.push_back('S');
		
		vector<char> v1, v2;
		bool imposs = true;
		do {
			v1 = v;
			v2.clear();
			bool tie2 = false;
			FOR(j, n){
				bool tie = false;
				for(int i = 0; i < SZ(v1); i += 2){
					char a = v1[i], b = v1[i + 1];
					if(a == b){
						tie = true;
						break;
					}
					v2.push_back(winner(a,b));
				}
				if(tie){
					tie2 = true;
					break;
				}
				assert(SZ(v2) * 2 == SZ(v1));
				v1 = v2;
				v2.clear();
			}
			if(tie2)
				continue;
			else {
				imposs = false;
				break;
			}
		} while(next_permutation(v.begin(), v.end()));
		
		if(imposs){
			ki<<"Case #"<<tt+1<<": "<<"IMPOSSIBLE"<<endl;
		} else {
			string res(v.begin(), v.end());
			ki << "Case #" << tt + 1 << ": " << res << endl;
		}
		//ki<<"Case #"<<tt+1<<": "<< <<endl;
	}

	ki.close();
	return 0;
}