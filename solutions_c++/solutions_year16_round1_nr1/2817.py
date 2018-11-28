#include <iostream>
#include <string>
using namespace std;
typedef long long ll;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

string S;
int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for1(t, T)
	{
		cout << "Case #" << t << ": ";
		cin >> S;
		string O="";
		O.push_back(S[0]);
		for (int i = 1; i < S.length(); i++)
		{
			if (S[i] < O[0])
				O.push_back(S[i]);
			else
				O.insert(O.begin(),1,S[i]);
		}
		cout << O << endl;
	}
	return 0;
}
