#include <bits/stdc++.h>
//this is sparta
using namespace std;

int l[] = {0, 1, 2, 3};
int g[] = {1, 4, 3, 6};
int h[] = {2, 7, 4, 1};
int k[] = {3, 2, 5, 4};
vector < vector <int> > f;


int multiply(int x, int y){
	if ( (x < 4) && (y < 4) )
	{
		return f[x][y];
	}
	if( (x<4) )
	{
		return (f[x][y-4] + 4) % 8;
	}
	if ( (y<4) )
	{
		return (f[x-4][y] + 4) % 8;
	}
	return f[x-4][y-4];
}

long long T, L, X, OP[100009], C[100009];
string S, final;

int main(int argc, char const *argv[])
{
    f.resize(4);
    f[0].assign(l, l+4);
    f[1].assign(g, g+4);
    f[2].assign(h, h+4);
    f[3].assign(k, k+4);
	cin >> T;
	for (int tt = 0; tt < T; ++tt)
	{
	    cin >> L >> X;
		cin >> S;
		final = "";
		for (int i = 0; i < X; ++i)
		{
			final += S;
		}
		for (int i = 0; i < (L*X); ++i)
		{
			OP[i] = final[i] - 'h';
		}
		C[0] = OP[0];
		for (int i = 1; i < (L*X); ++i)
		{
			C[i] = multiply( C[i-1], OP[i] );
		}
		int earlyI = 1<<30, lateK = -1;
		for (int i = 0; i < (L*X); ++i)
		{
			if ( C[i] == 1 )
			{
				earlyI = min(earlyI, i);
			}
			if ( C[i] == 3 )
			{
				lateK = max(lateK, i);
			}
		}
		string ans = "NO";
		if ( C[ (L*X) - 1] == 4 )
		{
			if ( (earlyI != (1<<30) ) && (lateK != -1) )
			{
				if ( earlyI < lateK )
				{
					ans = "YES";
				}
			}
		}
		cout << "Case #" << tt+1 << ": " << ans << '\n';
	}
	return 0;
}
