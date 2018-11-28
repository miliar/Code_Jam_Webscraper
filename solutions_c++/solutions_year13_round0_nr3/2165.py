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
mpz_class ref;

int provjeri1( mpz_class tmp )
	{
	if( tmp == 0 ) return 0;
	//cout << tmp << " " << ref << endl;
	string s = tmp.get_str();
	for( int i = (int)(s.size()) - 2; i>= 0; -- i )
		s += s[i];
	tmp = mpz_class( s );
	if( ref >= tmp * tmp ) return 1;
	return 0;
	}

int provjeri2( mpz_class tmp )
	{
	if( tmp == 0 ) return 0;
	//cout << tmp << endl;
	string s = tmp.get_str();
	for( int i = (int)(s.size()) - 1; i>= 0; -- i )
		s += s[i];
	tmp = mpz_class( s );
	if( ref >= tmp * tmp ) return 1;
	return 0;
	
	}


long long daj1( int duz, int srednji, mpz_class tmp )
	{
	long long sol = 0;
	if( duz == 0 )
		{
		sol += provjeri1( tmp );
		}
	else if( duz == 1 )
		{
		FOR(i, 0, 4 )
			if( srednji >= i*i )
				sol += daj1( 0, srednji - i*i, tmp*10+i);
		}
	else
		{
		FOR(i, 0, 4 )
			if( srednji >= 2*i*i )
				sol += daj1( duz-1, srednji - 2*i*i, tmp*10+i);
		}
	return sol;
	}
long long daj2( int duz, int srednji, mpz_class tmp )
	{
	long long sol = 0;
	if( duz == 0 )
		{
		sol += provjeri2( tmp );
		}
	else
		{
		FOR(i, 0, 3 )
			if( srednji >= 2*i*i )
				sol += daj2( duz-1, srednji - 2*i*i, tmp*10+i);
		}
	return sol;
	}

long long calc( mpz_class A )
	{
	int dg = 0; // full broj
	int korijen = 0; // korijen ( koji je isto palindrom )
	int polk = 0;
	mpz_class B = A;
	while( B > 0 )
		{ ++dg; B/=10; }
	korijen = (dg+1)/2;
	polk = (korijen+1)/2;
	long long sol = 0;
	ref = A;
	FOR( len, 1, polk+1)
		{
		//cout << len << endl;
		sol += daj1( len, 9, 0);
		sol += daj2( len, 9, 0);
		//cout << sol << endl;
		}
	return sol;
	}

int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( t, 0, T )
        {
        string s1, s2; cin >> s1 >> s2;        
	mpz_class A(s1), B(s2);
	//string s = A.get_str();
	//cout << s << endl;
	long long sol = calc(B) - calc(A-1);
	printf("Case #%d: %lld\n",t+1,sol);
        }
    return 0;
    }
