#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

struct Subtree
{
	Subtree()
	{
		num[0] = num[1] = num[2] = 0;
		rep = "";
	}
	Subtree(int idxW, int idxL)
	{
		num[0] = num[1] = num[2] = 0;
		num[idxW] = num[idxL] = 1;
		if (idxW == 0 || idxL == 0)
			rep.push_back('P');
		if (idxW == 1 || idxL == 1)
			rep.push_back('R');
		if (idxW == 2 || idxL == 2)
			rep.push_back('S');
	}
	int num[3];
	string rep;
};

Subtree combine(const Subtree& s1, const Subtree& s2)
{
	Subtree res;
	for (int i=0; i<3; i++)
		res.num[i] = s1.num[i] + s2.num[i];
	res.rep = (s1.rep < s2.rep ? s1.rep + s2.rep : s2.rep + s1.rep);
	return res;
}

Subtree solve(int idxW, int idxL, int N)
{
	if (N == 1)
		return Subtree(idxW, idxL);

	Subtree s1 = solve(idxW, (idxW+1)%3, N-1);
	Subtree s2 = solve(idxL, (idxL+1)%3, N-1);
	Subtree res = combine(s1, s2);

	//cerr << N << ": " << idxW << " vs. " << idxL << ": " << res.rep << " from " << s1.rep << " and " << s2.rep << endl;
	//cerr << "   " << res.num[0] << " " << res.num[1] << " " << res.num[2] << endl;

	return res;
}

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		int N, R, P, S;
		cin >> N >> R >> P >> S;

		bool any = false;
		string rep = "";

		Subtree s1 = solve(0, 1, N);
		if (s1.num[0] == P && s1.num[1] == R && s1.num[2] == S)
		{
			any = true;
			rep = s1.rep;
		}

		Subtree s2 = solve(1, 2, N);
		if (s2.num[0] == P && s2.num[1] == R && s2.num[2] == S)
			if (!any || s2.rep < rep)
			{
				any = true;
				rep = s2.rep;
			}

		Subtree s3 = solve(2, 0, N);
		if (s3.num[0] == P && s3.num[1] == R && s3.num[2] == S)
			if (!any || s3.rep < rep)
			{
				any = true;
				rep = s3.rep;
			}
		
		cout << "Case #" << t << ": ";
		if (any)
			cout << rep;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
    return 0;
}