#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second


bool ok[65];

void solve(int test)
{
	int n;
	cin >> n;
	int mask0 = 0;
	for (int i = 0; i < n*n; i++) 
	{
		char c;
		cin >> c;
		if (c == '1') mask0 |= (1<<i);
	}
	int ans = n*n - __builtin_popcount(mask0);
	int res = -1;
	for (int mask = 0; mask < (1<<(n*n)); mask++)
	{
		if ((mask & mask0) != mask0) continue;
		int con[4], rcon[4];
		for (int i = 0; i < n; i++)
		{
		   con[i] = (mask >> (i*n)) & ((1<<n)-1);
		   rcon[i] = 0;
		}
		for (int i = 0; i < n; i++)
		   for (int j = 0; j < n; j++)
		      rcon[j] |= ((mask>>(i*n+j))&1)<<i;
		ok[0] = 0;
		bool gok = 1;
		for (int mask2 = 1; mask2 < (1<<n); mask2++)
	    {
			int g = 0;
			for (int i = 0; i < n; i++)
			   if (((mask2>>i)&1)) g |= rcon[i];
			if (__builtin_popcount(g) <= __builtin_popcount(mask2)) ok[mask2] = 1;
			else ok[mask2] = 0;
			if (__builtin_popcount(g) < __builtin_popcount(mask2)) gok = 0;
			
			for (int i = 0; i < n; i++)
			   if (((mask2>>i)&1) && ok[mask2 ^ (1<<i)]) ok[mask2] = 1;
		//	cout << ok[mask2];
		}
		//cout << endl;
	//	if(gok) cout << "-" << mask << endl;
		for (int i = 0; i < n; i++)
		  if (!ok[con[i]]) gok = 0;
	//	if(gok) cout << "+" << mask << endl;
		//if (gok) cout << mask << endl;
		
		if (gok && __builtin_popcount(mask^mask0) < ans) 
		{
			ans =  __builtin_popcount(mask^mask0);
			res = mask;
			//cout << "mask=" << mask << endl;
			//for (int i = 0; i < (1<<n); i++) cout << ok[i];
			//cout << endl;
			//for (int i = 0; i < n; i++) cout << con[i] << endl;
	    }
	}
	
	cout << "Case #" << test << ": " << ans << endl;
	//cout << "res=" << endl;
	//for (int i = 0; i < n; i++,cout << endl)
	//   for (int j = 0; j < n; j++) cout << ((res>>(i*n+j))&1);
	//cout << endl;
	
}

int main()
{
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++) solve(i+1);
	return 0;
}
