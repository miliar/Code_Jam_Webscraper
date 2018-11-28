#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

string C[3] = {"P", "R", "S"};
int child[3] = {1, 2, 0};

vector<int> construct(int root, int level)
{
	if(level == 0)
	{
		vector<int> ret(3);
		ret[root] = 1;
		return ret;
	}
	else
	{
		vector<int> ret(3), A, B;
		A = construct(root, level-1);
		B = construct(child[root], level-1);
		for(int i = 0;i < 3;i++) ret[i] = A[i]+B[i];
		return ret;
	}
}

string plz(int root, int level)
{
	if(level == 0)
	{
		string ret = C[root];
		return ret;
	}
	else
	{
		string A = plz(root, level-1), B = plz(child[root], level-1);
		return min(A+B, B+A);
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int tt = 1;tt <= t;tt++) {
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	bool done = false;
	string res = "1";
	for(int i = 0;i < 3;i++)
	{
		if(construct(i, n) == vector<int>({p, r, s}))
		{
			//cout << plz(i, n) << "\n";
			if(res == "1") res = plz(i, n);
			else res = min(res, plz(i, n));
			done = true;
		}
	}
	cout << "Case #" << tt << ": ";
	if(!done) cout << "IMPOSSIBLE\n";
	else cout << res << "\n"; }
}