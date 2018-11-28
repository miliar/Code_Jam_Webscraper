#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const int MAXN = 1005;
int T, N;
char S[MAXN];

int min_stand()
{
	int cur = 0, ans = 0;
	for (int i = 0; i <= N; i++)
	{
		if (cur < i)
		{
			ans += i - cur;
			cur = i;
		}
		cur += S[i] - '0';
	}
	return ans;
}

int main()
{
	ifstream in ("input.txt");
	ofstream out ("output.txt");

	in >> T;
	for (int t = 1; t <= T; t++)
	{
		in >> N >> S;
		out << "Case #" << t << ": " << min_stand() << "\n";
	}

	in.close();
	out.close();
	return 0;
}