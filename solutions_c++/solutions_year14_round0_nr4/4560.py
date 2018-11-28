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
	ifstream be("D-large.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int n; be >> n;
		vector<double> ken(n), naomi(n);
		FOR(i, n)
			be >> naomi[i];
		FOR(i, n)
			be >> ken[i];
		sort(ALL(ken));  sort(ALL(naomi));
		auto orig_ken(ken), orig_naomi(naomi);
		int s2 = 0;
		FOR(i, n){
			auto it = lower_bound(ken.begin(), ken.end(), naomi[i]);
			if(it < ken.end()){
				ken.erase(it);
			} else {
				ken.erase(ken.begin());
				s2++;
			}
		}
		ken = orig_ken;  naomi = orig_naomi;
		int s1 = 0;
		int kf = 0, kl = n - 1;
		int nf = 0, nl = n - 1;
		FOR(i, n){
			if(naomi[nl] < ken[kf]){
				nf++;
				kl--;
			} else {
				auto it = lower_bound(naomi.begin(), naomi.end(), ken[kf]);
				naomi.erase(it);
				nl--;
				kf++;
				s1++;
			}
		}
		ki << "Case #" << tt + 1 << ": " << s1 << " " << s2 << endl;
	}


	ki.close();
	return 0;
}