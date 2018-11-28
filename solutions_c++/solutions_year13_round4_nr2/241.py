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
long long N, P;

bool mozeubacit( long long pos )
	{
	long long sol = 0;
	long long losiji = (1LL << N) - pos; long long svi = (1LL << N );

	FOR( i, 0, N )
		{
		if( losiji == 0 )
			{
			break;
			}
		sol += svi/2;
		svi /=2;
		losiji = (losiji-1)/2;
		}

	sol = (1LL << N) - sol;

	//cout << "ubacit " << pos << " " << sol << endl; 
	if( sol <= P )
		return 1;
	return 0;
	}

bool mozeizbacit( long long pos )
	{
	long long sol = 0;	
	long long bolji = pos - 1; long long svi = (1LL << N );
	sol = 1;
	FOR( i, 0, N )
		{
		if( bolji == 0 )
			{			
			break;
			}
		sol += svi/2;
		svi /=2;
		bolji = (bolji-1)/2;
		}
	//cout << "izbacit " << pos << " " << sol << endl; 
	if( sol <= P )
		return 0;
	else return 1;
	}
int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( tp, 0, T )
        {
        long long x1 = 0, x2 = 0;        
	cin >> N >> P;
	long long mx = (1LL << N);
	long long mn = 1;
	while( mx - mn )
		{
		long long md = (mn+mx+1)/2;
		if(mozeizbacit(md))
			mx = md-1;
		else mn = md;
		//cout << md << endl;
		}
	x1 = mn;
        mx = (1LL << N);
	mn = 1;
	while( mx - mn )
		{
		long long md = (mn+mx+1)/2;
		if(mozeubacit(md))
			mn = md;
		else mx = md-1;
		//cout << md << endl;		
		}
	x2 = mn;
        printf("Case #%d: %lld %lld\n",tp+1,x1-1,x2-1);
        }
    return 0;
    }
