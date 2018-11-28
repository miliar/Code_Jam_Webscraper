#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <cstring>
#include <stack>
#include <assert.h>
using namespace std;

#define IT(c) typeof((c).begin())

#define For(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define rep(x, n) For(x,0,n)
#define foreach(i, c) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define F first
#define S second

template<class T>
ostream& operator<<(ostream& out, vector<T> v){
	out << "[";
	rep(i, sz(v)){
		if(i) out << ", ";
		out << v[i];
	}
	out << "]";
	return out;
}
template<class A, class B>
ostream& operator<<(ostream& out, pair<A,B> p){
	out << "<" << p.F << ", " << p.S << ">";
	return out;
}
template<class T>
ostream& operator<<(ostream& out, set<T> s){
	out << "(";
	foreach(it, s){
		if(it != s.begin()) out << ", ";
		out << *it;
	}
	out << ")";
	return out;
}
template<class A, class B>
ostream& operator<<(ostream& out, map<A,B> m){
	out << "{";
	foreach(it, m){
		if(it != m.begin()) out << ", ";
		out << *it;
	}
	out << "}";
	return out;
}

typedef long long ll;

const int MAXN = 25;

bool check(vector<int>& val, vector<int>& pat){
	int best[MAXN];
	memset(best,0,sizeof(best));

	assert(sz(val) == sz(pat));
	rep(i, sz(val)){
		int hit = best[val[i]] + 1;
		if(hit != pat[i])
			return false;
		For(k, val[i]+1, MAXN)
			best[k] = max(best[k], hit);
	}
	return true;
}

int A[MAXN];
int B[MAXN];

int N;

int best[MAXN][MAXN];
bool used[MAXN];
int cur[MAXN];

bool rec(int pos){
	if(pos == N){
		int best2[MAXN];
		memset(best2,0,sizeof(best2));
		for(int i = N-1; i>=0; i--){
			int hit = best2[cur[i]] + 1;
			if(hit != B[i])
				return false;
			For(k, cur[i]+1, N)
				best2[k] = max(best2[k], hit);
		}
		return true;
	}

	rep(i,N) if(!used[i]){
		int hit = best[pos][i] + 1;
		if(hit != A[pos])
			continue;
		memcpy(best[pos+1], best[pos], N*sizeof(int));
		For(k, i+1, N)
			best[pos+1][k] = max(best[pos+1][k], hit);

		cur[pos] = i;
		used[i] = true;
		if( rec(pos+1) )
			return true;
		cur[pos] = -1;
		used[i] = false;
	}

	return false;
}


int main(){
int np; cin>>np;
rep(tp,np){
	cin>>N;
	rep(i,N){
		cin >> A[i];
	}
	rep(i,N)
		cin >> B[i];

	/*
	cout << "HERE: " << N  << endl;
	rep(i,N){
		cout << A[i] << " ";
	}
	cout << endl;

	rep(i,N){
		cout << B[i] << " ";
	}
	cout << endl;
	*/

	memset(used,0,sizeof(used));
	bool res = rec(0);
	assert(res);
	printf("Case #%d:", tp+1);
	rep(i,N){
		cout << " " << (cur[i]+1);
	}
	cout << endl;
}
	
}	
