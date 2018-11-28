#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<math.h>
#include<algorithm>
#include<string>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<conio.h>

using namespace std;

#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:100000000")
#define FOR(i, l, r, s)  for (int i = (l); i < (r); i += (s))
#define MFOR(i, l, r, s) for (int i = (l); i <= (r); i += (s))
#define DFOR(i, r, l, s) for (int i = (r); i >= (l); i -= (s))
#define ABS(a) (((a) > 0)? (a): -(a))
#define MIN(a, b) (((a) < (b)) ? (a): (b))
#define MAX(a, b) (((a) < (b)) ? (b): (a))
#define SQR(a) (a) * (a)
#define All(a) (a).begin(), (a).end()
#define PI 3.1415926535897932384626433832795
#define MEMS(a, b) memset((a), (b), sizeof(a))
#define MP make_pair
#define PB push_back
#define endl '\n'
#define LL long long
#define LD long double
#define U unsigned
#define X first
#define Y second

FILE *stream;

struct queries {

	LL l, r, num, sum;

	void read(int z) { cin >> l >> r; num = z; sum = 0; }
	void write() { printf("%ll %ll\n", l, r); }
};

const LL INFL = LL(1e18);
const int INF = int(1e9);
const int SIZE = int(1e6 + 10);
const int TSIZE = int(1e2 + 10);
const LD eps = 0.00001;
const int MOD = int(1e9 + 7);

void solution();
void accept();
LL POW(LL z, int step);
LL nod(LL a, LL b) { return a ? nod(b % a, a) : b; }

//scanf("%d", &a);
bool Comparator(string s1, string s2)
{
	string a1 = s1 + s2, a2 = s2 + s1;
	if (a1 < a2)
		return true;
	else
		return false;
}

void solution()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		accept();
	}
}

void accept()
{
	LL x, sum = 0, i = 0, cur = 0;
	bool used[10] = {0};
	cin >> x;
	if (x == 0)
	{
		cout << "INSOMNIA\n";
		return;
	}
	while (sum < 10)
	{
		i++;
		cur = x * i;
		while (cur > 0)
		{
			if (!used[cur % 10])
			{
				sum++;
				used[cur % 10] = 1;
			}
			cur /= 10ll;
		}
	}
	cout << x * i << endl;
}

LL POW(LL z, int step)
{
	if (step < 1)
		return 1;
	if (step == 1)
		return z;
	LL cur = POW(z, step / 2);
	cur *= cur;
	if (step % 2)
		cur *= z;
	return cur;
}

int main()
{
//#ifdef SpOleM98
	//freopen("input.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	double beg = clock();
	freopen("output.txt", "w", stdout);
//#endif
	srand(time(0));
	solution();
#ifdef SpOleM98
	double end = clock();
	fprintf(stderr, "*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
	//char ch = getche();
#endif
	return 0;
}