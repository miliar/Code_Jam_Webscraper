#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <string>

using namespace std;

string s[110];
long long ans;

vector < vector < pair < char, int> > > rep;

int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	int T = 0, N = 0, msize = 0;
	bool bad = false;

	cin >> T;

	for (int q = 0; q < T; q++)
	{
		ans = 0;
		cin >> N;
		rep.clear();
		msize = -1;
		bad = false;
		bool t = true;
		for (int i = 0; i < N; i++)
		{

			cin >> s[i];
			bool f = true;
			vector < pair < char, int> > tmp;
			for (int j = 0; j < s[i].size(); j++)
			{
				if ( f )
				{
					tmp.push_back( make_pair( s[i][j], 1 ) );
					f = false;
					continue;
				}
				
				if ( s[i][j] == tmp[ tmp.size() - 1 ].first )
				{
					tmp[ tmp.size() - 1 ].second++;
				} 
				else
				{
					tmp.push_back( make_pair( s[i][j], 1 ) );
				}
			}
			rep.push_back( tmp );
			if ( t )
			{
				msize = tmp.size();
				t = false;
			}
			else
				if ( tmp.size() != msize )
				{
					bad = true;
					break;
				}
		}
		
		for (int i = 0; i < msize; i++)
		{
			if ( bad )
				break;
			int tmin = rep[0][i].second, tmax = rep[0][i].second;
			for (int j = 1; j < N; j++)
			{
				if ( rep[j][i].first != rep[0][i].first )
				{
					bad = true;
					break;
				}
				tmin = min(tmin, rep[j][i].second);
				tmax = max(tmax, rep[j][i].second);
			}
			if ( bad )
				break;
			int temp = 0, bns = 1e6;
			for (int j = tmin; j <= tmax; j++)
			{
				temp = 0;
				for (int k = 0; k < N; k++)
				{
					temp += abs( j - rep[k][i].second );
				}
				bns = min(bns, temp);
			}
			ans += bns;
		}


		cout << "Case #" << q + 1 << ": ";
		if ( bad )
		{
			cout << "Fegla Won" << endl;
		} else
			cout << ans << endl;
	}
	return 0;
}
