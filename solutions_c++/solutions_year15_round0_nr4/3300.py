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

int T, X, R, C;
string ans[2] = {"RICHARD", "GABRIEL"};

int go()
{
	if (R > C)
		swap(R, C);

	if (X == 1)
		return 1;
	if (X == 2)
		return (R % 2 == 0) || (C % 2 == 0);
	if (X == 3)
		return (R == 2 && C == 3) || (R == 3 && C == 3) || (R == 3 && C == 4);
	return (R == 3 && C == 4) || (R == 4 && C == 4);
}

int main()
{
	ifstream in ("input.txt");
	ofstream out ("output.txt");

	in >> T;
	for (int t = 1; t <= T; t++)
	{
		in >> X >> R >> C;
		out << "Case #" << t << ": " << ans[go()] << "\n";
	}

	in.close();
	out.close();
	return 0;
}