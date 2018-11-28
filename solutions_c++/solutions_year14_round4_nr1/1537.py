#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <iomanip>
#include <cassert>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int N, X;
const int MAXN = 10000 + 9;
int S[MAXN];
bool used[MAXN];

struct cmp
{
	bool operator()(int a, int b)
	{
		return a > b;
	}
};

int solve(void)
{
	map<int, int, cmp> M;
	for (int i = 0; i < N; i++) M[S[i]]++;

	int result = 0;
	while (!M.empty())
	{
		result++;
		auto last = M.begin();
		int val=last->first;
		last->second--;
		if (last->second == 0) M.erase(val);

		int temp = X - val;
		auto possible = M.lower_bound(temp);
		if (possible != M.end())
		{
			possible->second--;
			if (possible->second == 0) M.erase(possible->first);
		}
	}

	return result;
	//sort(S, S + N);
	//for (int i = 0; i < N; i++) used[i] = false;
	//int result = 0;
}

void solve_A(void)
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (int tt = 1; tt <= T; tt++)
	{
		in >> N >> X;
		for (int i = 0; i < N; i++) in >> S[i];
		int temp = solve();
		out << "Case #" << tt << ": ";
		out << temp << '\n';
	}

	in.close();
	out.close();
}

int main()
{
	solve_A();
	//solve_B();
	//solve_C();
	return 0;
}

void solve_(void)
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (int tt = 1; tt <= T; tt++)
	{
		out << "Case #" << tt << ": ";
	}

	in.close();
	out.close();
}