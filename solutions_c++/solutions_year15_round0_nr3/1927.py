#include<iostream>
#include<cstdint>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<iterator>
#include<string>

using namespace std;
/*5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i*/

//char getv(string& S)
//{
//	char v = 1;
//	for (int i = 0; i < S.length(); ++i)
//	{
//		if (S[i] == 'i') 
//	}
//}


char getv(char a, char b)
{
	bool mi = (a > 0 != b > 0);
	char aa = abs(a);
	char ab = abs(b);

	char v = -1;
	if (aa == 'i' && ab == 'j') v =  'k';
	if (aa == 'i' && ab == 'k') v = -'j';
	if (aa == 'j' && ab == 'i') v = -'k';
	if (aa == 'j' && ab == 'k') v =  'i';
	if (aa == 'k' && ab == 'i') v =  'j';
	if (aa == 'k' && ab == 'j') v = -'i';
	if (aa == 1) v = ab;
	if (ab == 1) v = aa;
	return mi ? -v : v;
}

bool solve(string S, uint64_t X)
{
	if (S.length() * X < 3) return false;

	char v = 1;
	for (int j = 0; j < X; ++j)
	{
		for (int i = 0; i < S.length(); ++i)
		{
			v = getv(v, S[i]);
		}
	}

	//if ((v == -1 && (X % 2 == 0)) || v == 1 || (v != -1 && (X % 2 != 0))) return false;
	if (v != -1) return false;

	bool fi = false;
	v = 1;
	int ci = 0;
	for (int j = 0; j < X && !fi; ++j)
	{
		for (int i = 0; i < S.length() && !fi; ++i)
		{
			v = getv(v, S[i]);
			if (v == 'i') fi = true;
			++ci;
		}
	}
	if (!fi) return false;

	bool fk = false;
	v = 1;
	int ck = 0;
	for (int j = 0; j < X && !fk; ++j)
	{
		for (int i = S.length() - 1; i >= 0 && !fk;--i)
		{
			v = getv(S[i], v);
			if (v == 'k') fk = true;
			++ck;
		}
	}
	if (!fk) return false;
	return (ci + ck) < (S.length() * X);
}

int main()
{
	uint64_t T;
	cin >> T;

	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t L, X;
		cin >> L >> X;
		string S;
		cin >> S;

		auto s = solve(S, X);

		cout << "Case #" << t + 1 << ": " << (s ? "YES" : "NO" ) << endl;
	}
	return 0;
}
