#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

double an[1005], ak[1005];
bool usd[1005];
int n;

int main()
{
	freopen("D-large.in", "r", stdin);
	//freopen("Dinput.txt", "r", stdin);
	freopen("Doutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		cin >> n;
		for(int i = 0; i < n; ++i)
			cin >> an[i];
		for(int i = 0; i < n; ++i)
			cin >> ak[i];
		sort(an, an+n);
		sort(ak, ak+n);

		int qw = 0;
		memset(usd, 0, sizeof(usd));
		for(int i = 0; i < n; ++i)
		{
			bool fnd = 0;
			for(int j = 0; j < n; ++j)
				if(!usd[j] && ak[j] > an[i])
				{
					usd[j] = 1;
					fnd = 1;
					break;
				}
			if(fnd) continue;
			++qw;
			for(int j = 0; j < n; ++j)
				if(!usd[j])
				{
					usd[j] = 1;
					break;
				}
		}

		int qdw = 0;
		for(int k = 1; k <= n; ++k)
		{
			int q = 0;
			for(int i = 0; i < k; ++i)
				if(an[n-k+i] > ak[i])
					++q;
			if(q != k)
				break;
			qdw = k;
		}

		printf("Case #%d: %d %d\n", tt, qdw, qw);
		

	}
	
	return 0;
}