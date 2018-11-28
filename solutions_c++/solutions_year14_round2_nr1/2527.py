#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdlib>
#include <string>
#include <sstream>
#include <gmpxx.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define VVI vector< VI >
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it!=(kont).end(); ++it)

char buff[20000];

VVI kol;
VS imp;

void srezi(string s, int ind)
	{
	string bla;
	char last = '.';
	VI sizes;
	
	FOR(i,0,s.size())
		{
		if( last == s[i] )
			sizes.back()++;
		else
			{
			sizes.pb(1);
			bla += s[i];
			last = s[i];
			}
		}
	kol[ind] = sizes;
	imp[ind] = bla;
	}

int sumiraj(int ind)
	{
	VI x;
	FOR(i,0,kol.size())
		x.pb(kol[i][ind]);
	sort(x.begin(),x.end());
	int m = x.size()/2;
	int res =0;
	FOR( i, 0, x.size() )
		res += abs(x[i] - x[m]);
	return res;	
	}

int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( t, 0, T )
        {
        int sol = 0;
	int N;
	cin >> N;
	VS rijeci(N);
	FOR(i,0,N) cin >> rijeci[i];
	kol.clear(); kol.resize(N);
	imp.clear(); imp.resize(N);
	
	FOR(i,0,N) 
		srezi(rijeci[i],i);		

	//FOR(i,0,N)
	//	{
	//	cout << imp[i] << endl;
	//	}

	int ok = 1;

	FOR(i,0,N-1)
		if( imp[i] != imp[i+1] )
			ok = 0;

	FOR(i,0,kol[0].size())
		sol += sumiraj(i);

	if( ok == 1) 
		printf("Case #%d: %d\n",t+1,sol);
	else 
		printf("Case #%d: Fegla Won\n",t+1);
        }
    return 0;
    }
