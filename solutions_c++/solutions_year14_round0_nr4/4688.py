/*
vector< vector<int> > Matrix(10, vector<int>(20, -1));
iterator max_element(range);
iterator min_element(range);
sort ALLR descending
string s
istringstream is(s); is >> x;
ostringstream os(s); os << x;

for (auto x : container)
{
cout << x << endl;
}

for_each(v.begin(), v.end(),
[&] (int x) {
cout << x << endl;
}
)


*/

/*
------------------------------------------------------------------
void dfs(int i) {
if (!V[i]) {
V[i] = true;
for_each(all(W[i]), dfs);
}
}

bool check_graph_connected_dfs() {
int start_vertex = 0;
V = vi(N, false);
dfs(start_vertex);
return (find(all(V), 0) == V.end());
}

void add(int poz, int val) {
for (; poz <= N; poz += zeroes(poz)) {
aib[poz] += val;
}
}

long long compute(int poz) {
long long sum = 0;
for (; poz; poz -= zeroes(poz)) {
sum += aib[poz];
}
return sum;
}
*/

#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cstdio>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <cassert>
#include <iomanip>

using namespace std;

//```
#define ONLINE_JUDGE1

const double epsilon = 1e-7;
#define LL long long
#define ULL unsigned long long 

typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef pair<long long, long long> ll;
typedef vector<ii> vii;
typedef vector<ll> vll;

#define all(V) V.begin(), V.end()
#define allr(V) V.rbegin(), V.rend()
#define for_c_it(container, it) for (auto it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end()) 
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair
#define zeroes(x) ((x ^ (x - 1)) & x)

void solve();

int main() {
#ifndef ONLINE_JUDGE
	freopen("p3.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
#ifndef ONLINE_JUDGE
	//while (true);
#endif
	return 0;
}

void solve() {
	vd A, B;
	int N, i, j;
	scanf("%d", &N);
	A.resize(N);
	B.resize(N);
	for (int i = 0; i < N; ++i) {
		scanf("%lf", &A[i]);
	}
	for (int i = 0; i < N; ++i) {
		scanf("%lf", &B[i]);
	}
	set <double> sett, sed;
	for (i = 0; i < N; ++i) {
		sett.insert(B[i]);
		sed.insert(B[i]);
	}
	sort(all(A));
	sort(all(B));
	i = N - 1;
	int W = 0, DW = 0;
	while (i >= 0) {
		auto it = sett.upper_bound(A[i]);
		if (it == sett.end()) {
			++W;
			sett.erase(*sett.begin());
		}
		else {
			sett.erase(it);
		}
		--i;
		
	}
	i = 0;
	j = N - 1;
	while (i < N) {
		if (A[i] - *sed.begin() > epsilon) {
			++DW;
			sed.erase(sed.begin());
		}
		else {
			sed.erase(*sed.rbegin());
		}
		++i;
	}
	printf("%d %d\n", DW, W);
	
}