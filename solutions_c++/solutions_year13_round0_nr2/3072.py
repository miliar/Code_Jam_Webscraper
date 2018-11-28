#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <cstring>

using namespace std;

int F[128][128], T, w, h;
int R[128], C[128];

int main (int argc, char const* argv[])
{
    ifstream cin ("B-large.in");
	ofstream cout ("B-large.out");
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
	    memset(R, 0, sizeof(R));
	    memset(C, 0, sizeof(C));

		cin >> w >> h;
		for (int i = 0; i < w; i += 1)
		{
			for (int j = 0; j < h; j += 1)
			{
				cin >> F[i][j];
			}
		}
		for (int i = 0; i < w; i += 1)
		{
			for (int j = 0; j < h; j += 1)
			{
				R[i] = max (R[i], F[i][j]);
				C[j] = max (C[j], F[i][j]);
			}
		}
		int flag = 1;
		for (int i = 0; i < w; i += 1)
		{
			for (int j = 0; j < h; j += 1)
			{
				if ( F[i][j] != min( C[j], R[i]) )
				{
					flag = 0;
				}
			}
		}
        	if( flag == 1)
		        cout << "Case #" << t+1 << ": " << "YES"<< "\n";
		else
			cout << "Case #" << t+1 << ": " << "NO"<< "\n";
	}
	return 0;
}
