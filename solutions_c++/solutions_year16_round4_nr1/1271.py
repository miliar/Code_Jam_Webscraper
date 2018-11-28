#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>
#define _ << " _ " <<
#define dbg(x) cerr << #x << " == " << x << endl
#define mp(x,y) make_pair((x),(y))
#define pv(x,y) {for(typeof(y) z=(x);z!=(y);z++)cerr<<*z<<" ";cerr<<endl;}
#define rep(x,y) for(int(x)=(0);(x)<int(y);++(x))
#define x first
#define y second
using namespace std;

typedef long long ll;
typedef pair<int,int> pt;

#if 0
#define GENERATE 1
#endif

int N, R, P, S;

int r, p, s;
void get(vector<int> v) {
	r=p=s=0;
	for (int i = 0; i < v.size(); i++) {
		int x = v[i];
		if(x==0) p++;
		if(x==1) r++;
		if(x==2) s++;
	}
}

vector<int> ANS;

int  solve(int n, vector<int> v) {
	get(v);
	if(p>P || r>R || s>S) return 0;
	if(n==N) {
		if(ANS.size()==0) ANS=v;
		else if(v < ANS)  ANS=v;
		return 1;
	}
	return 0;
}

vector<int> opt(vector<int> v) {
	for(int i = 2; i <= v.size(); i = i*2) {
		vector<int> nv;
		for (int j = 0; j < v.size(); j += i) {
			vector<int> a, b;
			for (int r=0;r<i/2;r++) {
				a.push_back(v[j+r]);
				b.push_back(v[j+i/2+r]);
			}
			vector<int> c = min(a,b);
			vector<int> d = max(a,b);
			for(int r=0;r<i/2;r++) nv.push_back(c[r]);
			for(int r=0;r<i/2;r++) nv.push_back(d[r]);
		}
		v=nv;
	}
	return v;
}

vector<int> f(vector<int> v) {
	vector<int> ans;
	for (int i = 0; i < v.size(); i++) {
		int x = v[i];
		if (x == 0) {
			ans.push_back(0);
			ans.push_back(1);
		} else if (x == 1) {
			ans.push_back(1);
			ans.push_back(2);
		} else {
			ans.push_back(0);
			ans.push_back(2);
		}
	}
	return ans;
}

vector<int> F[13];
vector<int> G[13];
vector<int> H[13];



void go() {
	vector<int> p, r, s;
	p.push_back(0);
	r.push_back(1);
	s.push_back(2);

	F[0] = p;
	G[0] = r;
	H[0] = s;

	for (int i = 1; i <= 12; i++) {
		F[i] = opt(f(F[i-1]));
		G[i] = opt(f(G[i-1]));
		H[i] = opt(f(H[i-1]));
	}
}

void read() {
	cin >> N >> R >> P >> S;
}


void process() {
	vector<int> ans;
	
	get(F[N]);
	if(p==P && r==R && s==S) {
		if(ans.size()==0 || F[N]<ans) ans = F[N];
	}

		get(G[N]);
	if(p==P && r==R && s==S) {
		if(ans.size()==0 || G[N]<ans) ans = G[N];
	}

		get(H[N]);
	if(p==P && r==R && s==S) {
		if(ans.size()==0 || H[N]<ans) ans = H[N];
	}

	if(ans.size()==0) {
		cout<<" IMPOSSIBLE"<<endl;
	}
	else {
		cout<<" ";
		for (int i = 0; i < ans.size(); i++) {
			int x = ans[i];
			if(x==0) cout<<"P";
			if(x==1) cout<<"R";
			if(x==2) cout<<"S";
		}
		cout<<endl;
	}
}

int main() {

	go();

	int T;
#ifdef GENERATE
	unsigned int seed=time(0);
	dbg(seed);
	srand(seed);
	T=50;
	for(int testcase=1;testcase<=T;++testcase) {
		fprintf(stderr,"Case #%d:",testcase);
		// *generate input!
		// BEGIN
		// END
#else
		cin>>T;
		for(int testcase=1;testcase<=T;++testcase) {
			fprintf(stdout,"Case #%d:",testcase);
			read();
#endif
		try {
			process();
		} catch(char const*exception) {
			puts(exception);
		}
	}
	return 0;
}
