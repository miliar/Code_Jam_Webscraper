#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

typedef map<int, int, greater<int> > IntMapDesc;

int round(double x)
{
	return int(x + 0.5);
}

int solve(IntMapDesc &P, IntMapDesc::iterator &it, const int &th)
{
	if (it == P.end())
	{
		return 0;
	}

	if (it->first <= th)
	{
		return it->first;
	}

	IntMapDesc::iterator tit = it;
	int y = 0;
	int d = tit->first / th;
	P[th] += tit->second * d;
	it++;
	if (tit->first % th == 0)
	{
		d--;
	}
	int t = tit->second * d + solve(P, it, th);
	y = (t < tit->first ? t : tit->first);

	return y;
}

int solve(IntMapDesc &P)
{
	int maxv = P.begin()->first;
	int miny = 1000;

	for (int i = round(maxv * 0.5); i >= 2; i--)
	{
		IntMapDesc tP(P.begin(), P.end());
		int t = solve(tP, tP.begin(), i);
		miny = miny < t ? miny : t;
	}

	miny = miny < maxv ? miny : maxv;

	return miny;
}

int main()
{
//	string name = "B-small-attempt1";
// 	ifstream in(name + ".in", ios::in);
// 	ofstream out(name + ".out", ios::out);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int D;
		cin >> D;
		IntMapDesc P;
		for (int j = 0; j < D; j++)
		{
			int tmp;
			cin >> tmp;
			P[tmp]++;
		}

		int y = solve(P);
		cout << "Case #" << i << ": " << y << endl;
	}

	return 0;
}