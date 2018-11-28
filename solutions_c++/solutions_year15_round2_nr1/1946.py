
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef long double ld;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Max(a,b) (a)<(b)?(b):(a)
#define Min(a,b) (a)<(b)?(a):(b)

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024];

typedef uint64_t ans_t;

ans_t SolveMain(uint64_t N);

int Sol[1000001];

int GetReverse(int e, int *e1)
{
	if (e % 10 == 0)
		return -1;
	
	int  rev = 0;
	int  org = e;
	while (org > 0)
	{
		int d = org % 10;
		org = (org - d) / 10;
		rev = rev * 10 + d;
	}
	
	if (e == rev)
		return -1;
	
	*e1 = rev;
	return 0;
}

int Prepare()
{
	for (int i = 1; i <= 1000001; i++)
	{
		Sol[i] = -1;
	}

	int Q1_[1000000];
	int Q2_[1000000];
	int *Q1 = Q1_;
	int *Q2 = Q2_;
	int q1_size = 0;
	int q2_size = 0;
	int k = 1;

	Sol[1] = k;
	Q1[q1_size++] = 1;

	do 
	{
		k++;
		for (int i = 0; i < q1_size; i++)
		{
			int e = Q1[i];
			if (e+1 <= 1000000 && Sol[e + 1] == -1)
			{
				Sol[e + 1] = k;
				Q2[q2_size++] = e + 1;
			}
			int e1;
			int ret = GetReverse(e, &e1);
			if (ret < 0)
				continue;
			if (e1 <= 1000000 && Sol[e1] == -1)
			{
				Sol[e1] = k;
				Q2[q2_size++] = e1;
			}
		}

		int *t = Q1;
		Q1 = Q2;
		Q2 = t;
		q1_size = q2_size;
		q2_size = 0;
	} while (q1_size > 0);

	return 0;
}

int main() {
	Prepare();

	fgets(buf, 1024, stdin);
	int T = atoi(buf);
	For(tcase, 1, T) {
		uint64_t N;
		scanf("%llu", &N);

// 		printf("%llu\n", N);

		ans_t ans = SolveMain(N);

		printf("Case #%d: %llu", tcase, ans);
		printf("\n");
	}
}


ans_t SolveMain(uint64_t N)
{
	return Sol[N];
}

