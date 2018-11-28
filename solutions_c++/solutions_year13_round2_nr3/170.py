#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:106777216")
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
#include <cstdarg>
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
void print(const char *fmt, ...)  { va_list args; va_start(args, fmt); vprintf(fmt, args); vfprintf(stderr, fmt, args); va_end(args); }

class Node 
{
public:
	bool isFinal;
	(Node*) children['z'-'a'+1];
};

char s[5000];

Node root;
int N, M, K;
int m[4011][10];

void addWord(Node* node, char *w)
{
	Node* n = node;
	for(int i=0; w[i]; ++i)
	{
		int l = w[i] - 'a';
		Node* &nn = n->children[l];
		if (!nn)
			nn = new Node();
		n = nn;
	}
	n->isFinal = true;
}

int match_word(Node* node, int p, int errPos, int penalty);
int solve(int p, int errPos)
{
	int& r = m[p][min(5, p - errPos)];
	if (r != -1) return r;

	if (p == N) return r = 0;
	return r = match_word(&root, p, errPos, 0);
}

int match_word(Node* node, int p, int errPos, int penalty)
{
	if (!node) throw -1;
	if (p == N) return inf;

	int res = inf;
	Node* n = node->children[s[p]-'a'];
	if (n) 
	{
		if (n->isFinal)
			res = min(res, penalty + solve(p+1, errPos));
		res = min(res, match_word(n, p+1, errPos, penalty));
	}

	if (p - errPos >= 5)
	{
		for (int i='a'; i<='z'; ++i)
		{
			if (s[p] == i) continue;
			Node* n2 = node->children[i-'a'];
			if (n2)
			{
				if (n2->isFinal)
					res = min(res, penalty + 1 + solve(p+1, p));
				res = min(res, match_word(n2, p+1, p, penalty+1));
			}
		}
	}
	return res;
}

int main()
{
	freopen("inC.txt", "r", stdin);
	freopen("outC.txt", "w", stdout);
	clock_t startTime = clock();

	FILE* f = fopen("garbled_email_dictionary.txt", "r");
	//int cnt=0;
	while (fscanf(f, "%s\n", s) == 1)
	{
		addWord(&root, s);
		//if (cnt++ % 1000 == 0) 			print("Processed %d...\n", cnt);
	}
	//return 0;

	int Cases;
	scanf("%d\n", &Cases);
	FOR(Case,0,Cases)
	{
		print("Case #%d: ", Case+1);

		fill(m, -1);
		gets(s);
		N = strlen(s);
		int r = solve(0, -5);
		print("%d\n", r);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
