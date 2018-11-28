#include <bits/stdc++.h>
using namespace std;

const int SAMPLES = 10000;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
	assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) { 
	if (debug) {
		va_list pvar;
		va_start(pvar, err);
		return vfprintf(stderr, err, pvar);
	}
	return 0;
}


int N;
vi children[200];
int sz[200];
string sym;

int Size(int x) {
	if (sz[x] == 0) {
		sz[x] = 1;
		for (auto y: children[x]) sz[x] += Size(y);
	}
	return sz[x];
}

string sample(vi &roots) {
	int N = 0;
	vi F;
	for (auto r: roots) {
		F.push_back(Size(r));
		N += F.back();
	}
	if (!N) return "";
	int choice = random() % N;
	for (int i = 0; i < F.size(); ++i) {
		if (choice < F[i]) {
			int r = roots[i];
			roots.erase(roots.begin()+i);
			for (auto c: children[r]) {
				roots.push_back(c);
			}
			return sym[r] + sample(roots);
		} else {
			choice -= F[i];
		}
	}
	assert(0);
}

void solve(int P) {
	int N;
	cin >> N;
	vi initroots;
	for (int i = 0; i < N; ++i) {
		children[i].clear();
		sz[i] = 0;
	}
	
	for (int i = 0; i < N; ++i) {
		int p;
		cin >> p;
		if (p == 0) initroots.push_back(i);
		else children[p-1].push_back(i);
	}
	cin >> sym;
	int M;
	cin >> M;
	string words[100];
	int hits[100];
	for (int i = 0; i < M; ++i) {
		cin >> words[i];
		//reverse(words[i].begin(), words[i].end());
		hits[i] = 0;
	}
	for (int i = 0; i < SAMPLES; ++i) {
		vi roots = initroots;
		string x = sample(roots);
		for (int i = 0; i < M; ++i) {
			if (x.find(words[i]) != string::npos)
				++hits[i];
		}
	}
	printf("Case #%d:", P);
	for (int i = 0; i < M; ++i)
		printf(" %.4lf", 1.0*hits[i]/SAMPLES);
	printf("\n");
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) {
		solve(i);
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
