#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>

#define FOR(a,b,c) for (int c = (a), _for = (b); c < _for; ++c)
#define REP(n) for (int _rep = 0, _for = (n); _rep < _for; ++_rep)
#define pb push_back
#define x first
#define y second
#define ll long long
#define ull unsigned ll
#define pii pair < int, int >

using namespace std;

class BitSet{
public:
	static const ull one = 1;
	ull T[50];
	void clear(){memset(T, 0, sizeof T);}
	BitSet(){clear();}
	void set(int p){T[p / 64] |= (one << (p & 63));}
};

int n;
map < string, int > M;
vector < int > V[205];
BitSet A, B;

int Counter;
int add(string s){
	if (M.count(s)) return M[s];
	return M[s] = Counter++;
}

char in[100005];
vector < int > ReadLine(){
	gets(in);
	string tmp;
	vector < int > R;
	for (auto x : in){
		if (x == '\0') break;
		if (x == ' '){
			if (tmp.size()) R.pb(add(tmp)), tmp.clear();
		}
		else tmp.pb(x);
	}
	if (tmp.size()) R.pb(add(tmp));
	return R;
}

BitSet At, Bt;

int Count(int bit){
	A = At, B = Bt;
	FOR(2, n, i){
		bool ch = (bit & 1);
		bit >>= 1;
		if (ch) for (auto x : V[i]) A.set(x);
		else for (auto x : V[i]) B.set(x);
	}
	int R = 0;
	FOR(0, 50, i) R += __builtin_popcountll(A.T[i] & B.T[i]);
	return R;
}

void Solve(){
	Counter = 1;
	M.clear();
	At.clear();
	Bt.clear();
	for (auto &x : V) x.clear();
	scanf("%d", &n); gets(in);
	FOR(0, n, i) V[i] = ReadLine();
	for (auto x : V[0]) At.set(x);
	for (auto x : V[1]) Bt.set(x);
	int Sol = Count(0);
	FOR(1, 1 << (n - 2), i) Sol = min(Sol, Count(i));
	printf("%d\n", Sol);
}

int main(){
	int t;
	scanf("%d", &t);
	FOR(1, t + 1, i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}

