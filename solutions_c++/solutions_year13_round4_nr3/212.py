
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

int N, A[20], B[20];
int need1[20];
int need2[20];
int may[20];
int bits[1<<20];
string smallest[1<<20];
void calc(){
	bits[0] = 0;
	FOR(i,1, 1<< 20)bits[i] = 1 + bits[i ^ (i&-i)];
	cin >> N;
	FOR(i,0,N)cin >> A[i];
	FOR(i,0,N)cin >> B[i];
	memset(need1,0,sizeof(need1));
	memset(need2,0,sizeof(need2));
	memset(may,0,sizeof(may));
	FOR(i,0,N){
		FOR(j,0,i)if(A[j] < A[i])may[i] |= 1<<j;
		FOR(j,i+1,N)if(B[j] < B[i])may[i] |= 1<<j;
		FOR(j,0,i)if(A[j] + 1 == A[i])need1[i] |= 1<<j;
		FOR(j,i+1,N)if(B[j] + 1 == B[i])need2[i] |= 1<<j;
	}
	FOR(i,0,1<<N)smallest[i] = "Z";
	smallest[0] = string(N,'A');
	FOR(i,0,1<<N){
		if(smallest[i] == "Z")continue;
		//FOR(p,0,N)cout << ((i>>p)&1);
		//cout << " " << smallest[i] << endl;
		FOR(p,0,N)if(((i>>p)&1) == 0){
			//cout << p <<":";
			//cout << "H1\n";
			if((may[p]&i) != i)continue;
			//cout << "H2\n";
			if(A[p] > 1 && (need1[p] & i) == 0)continue;
			//cout << "H3\n";
			if(B[p] > 1 && (need2[p] & i) == 0)continue;
			//cout << "H4\n";
			string cur = string(smallest[i]);
			cur[p] = (char) ('B'+bits[i]);
			//cout << cur << endl;
			int oth = i | (1<<p);
			if(smallest[oth] > cur){
				smallest[oth] = cur;
				//cout << "BLA\n";
			}
//			smallest[i|(1<<p)] == min(smallest[i|(1<<p)], cur);
		}
	}
	string tmp = smallest[(1<<N) - 1];
	FOR(i,0,N){
		int ai = 1;
		FOR(j,0,i)if(tmp[j] < tmp[i])ai = max(ai, 1 + A[j]);
		if(ai != A[i])cout << "ERROR\n";
	}
	FOR(i,0,N)cout << " " << (int)(tmp[i] - 'B' + 1);
//	cout << smallest[(1<<N) - 1] << endl;
}

int main() {
	int tc;
	cin >> tc;
	FOR(tcc, 1, tc + 1){
		cout << "Case #" << tcc << ":";
		calc();
		cout << endl;
	}
	return 0;
}
