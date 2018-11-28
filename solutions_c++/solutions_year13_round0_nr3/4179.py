#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
typedef long long ll;
const int MAXK = 10000100;

ifstream fin ("C.in");
ofstream fout ("C.out");

bool pal (ll x)
{
	int dig[20];
	int ndig = 0;
	while (x)
	{
		dig[ndig] = x % 10;
		ndig++;
		x /= 10;
	}
	
	for (int i = 0; i < ndig; i++)
		if (dig[i] != dig[ndig-1-i])
			return false;
	return true;
}

bool cpal[MAXK];

int main()
{
	int T; fin >> T;
	
	for (int x = 1; x <= 1e7; x++)
		cpal[x] = pal (x);
	
	for (int test = 1; test <= T; test++)
	{
	
	ll A, B;
	fin >> A >> B;
	
	int ans = 0;
	for (ll x = 1; x <= 1e7; x++)
	{
		if (cpal[x] && A <= x * x && x * x <= B && pal (x * x))
			ans++;
	}
	
	fout << "Case #" << test << ": " << ans << "\n";
	}
	
	return 0;
}
