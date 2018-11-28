#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

vector <string> v;

string bucket[100];
int N;

int prefix(const string &a, const string &b) {
	int i;

	for(i = 0; i < sz(a) && i < sz(b) && a[i] == b[i]; i++);
	return i;
}

pair<int,int> backtrack(int i) {
	int j;
	int c,m = -1;
	int ways = -1;
	pair<int,int> ret;
	string p;

	if(i >= sz(v)) {
		return make_pair(0,1);
	}

	Fj(N) {
		p = bucket[j];
		c = sz(v[i]) - prefix(p,v[i]);
		if(sz(p) == 0) c++;
		bucket[j] = v[i];
		ret = backtrack(i+1);
		//printf("%s after %s => %d %d\n",v[i].c_str(),p.c_str(),c,ret.first);
		c += ret.first;
		bucket[j] = p;

		if(c > m) {
			m = c;
			ways = ret.second;
		} else if (m == c) {
			ways = (ways + ret.second) % 1000000007;
		}
	}
	//printf("return %s => %d %d\n",v[i].c_str(), m, ways);
	return make_pair(m,ways);
}

int main() {
	int T,cs;
	int M;
	char s[1000];
	int i;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&M,&N);

		v.clear();
		while(M--) {
			scanf("%s",s);
			v.push_back(s);
		}	
		sort(all(v));

		Fi(N) bucket[i] = "";

		pair<int,int> p = backtrack(0);

		printf("Case #%d: %d %d\n",cs,p.first,p.second);
	}

	return 0;
}
