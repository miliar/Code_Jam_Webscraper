#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

#define IMPOSSIBLE "IMPOSSIBLE"


int read() {
	int tmp;
	scanf("%d", &tmp);
	return tmp;
}

int n, r, p, s;
bool found;

int cnt[200];

int outN;
char out[2000];
int solN;
char sol[2000];

void sort(int a, int b)
{
	if (b - a == 1) return;

	int m = (a + b) / 2;

	sort(a, m);
	sort(m, b);

	int len = (b - a) / 2;

	int i = 0;
	while (i < len && out[a + i] == out[m + i])
	{
		i++;
	}

	if (i < len && out[a + i] > out[m + i])
	{
		for (int j = 0; j < len; j++)
		{
			char t = out[a + j];
			out[a + j] = out[m + j];
			out[m + j] = t;
		}
	}
}

void reset() {
	n = r = p = s = 0;
	found = false;
	for (int i = 0; i < 2000; i++) sol[i] = 0;
	for (int i = 0; i < 200; i++) cnt[i] = 0;
	
	outN = 0;
	for (int i = 0; i < 2000; i++) out[i] = 0;
	solN = 0;
	for (int i = 0; i < 2000; i++) sol[i] = 0;

}

void readInput() {
	n = read();
	r = read();
	p = read();
	s = read();
}

char looser(char winner)
{
	if (winner == 'P') return 'R';
	if (winner == 'R') return 'S';
	if (winner == 'S') return 'P';
	return 0;
}


void generate(int lvl, char p)
{
	if (lvl == n)
	{
		out[outN++] = p;
		return;
	}

	char l = looser(p);
	if (cnt[l])
	{
		cnt[l]--;
		generate(lvl + 1, p);
		generate(lvl + 1, l);
	}
}

void replace()
{
	solN = outN;
	for (int i = 0; i < solN; i++)
	{
		sol[i] = out[i];
	}
}

void tryP(char pp)
{

	cnt['P'] = p;
	cnt['R'] = r;
	cnt['S'] = s;

	if (cnt[pp] == 0) { return; }
	cnt[pp]--;

	outN = 0;
	generate(0, pp);

	if (cnt['P'] == 0 && cnt['R'] == 0 && cnt['S'] == 0)
	{
		found = true;

		sort(0, outN);
		if (solN == 0) replace();
		else {
			for (int i = 0; i < outN; i++)
			{
				if (sol[i] != out[i])
				{
					if (sol[i] > out[i]) replace();
					break;
				}
			}
		}
	}
}

int solve() {
	tryP('P');
	tryP('R');
	tryP('S');


	if (!found)
	{
		printf("%s", IMPOSSIBLE);
	}
	else
	{
		printf("%s", sol);
	}

	cout << endl;

	return 0;
}

bool stop;

char tmp[2000];

bool test2()
{
	outN = 1 << n;
	int n = outN;

	for (int i = 0; i < n; i++)
	{
		tmp[i] = out[i];
	}

	while (n > 1)
	{
		for (int i = 0; i < n; i += 2)
		{
			if (tmp[i] == looser(tmp[i + 1]))
			{
				tmp[i / 2] = tmp[i + 1];
			}
			else if (tmp[i+1] == looser(tmp[i]))
			{
				tmp[i / 2] = tmp[i];
			}
			else {
				return false;
			}

		}
		n /= 2;
	}
	return true;
}

void generate2(int i, int n)
{
	if (stop) return;

	if (i == n)
	{
		if (test2())
		{
			printf("%s\n", out);
			stop = true;
		}
		return;
	}

	char t = 'P';
	if (cnt[t] > 0)
	{
		cnt[t]--;
		out[i] = t;
		generate2(i + 1, n);
		cnt[t]++;
	}
	t = 'R';
	if (cnt[t] > 0)
	{
		cnt[t]--;
		out[i] = t;
		generate2(i + 1, n);
		cnt[t]++;
	}
	t = 'S';
	if (cnt[t] > 0)
	{
		cnt[t]--;
		out[i] = t;
		generate2(i + 1, n);
		cnt[t]++;
	}

}

void solve2()
{
	cnt['P'] = p;
	cnt['R'] = r;
	cnt['S'] = s;

	stop = false;
	outN = 0;
	generate2(0, 1 << n);
	if (!stop) printf("%s\n", IMPOSSIBLE);
}

void printTestCaseHeader(int testIndex) {
	cout << "Case #" << testIndex << ": ";
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int __T;
	scanf("%d", &__T);

	for (int i = 1; i <= __T; i++)
	{
		cerr << i << endl;
		reset();
		readInput();
		printTestCaseHeader(i);
		solve();
		//solve2();
		//cout << endl;
	}

	return 0;
}
