#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define P pair< int, int >
using namespace std;

ifstream fin( "A-small-attempt0.in" );
ofstream fout( "A1.in" );
#define cin fin
#define cout fout


char v[] = {'a', 'e', 'i', 'o', 'u'};

int isV( char ch ){
	for( int i = 0; i < 5; i++ )
		if( v[i] == ch )
			return 0;
	return 1;
}

string s;
int test, T = 1, n;

int main()
{
	for( cin >> test; test--; ){
		int res = 0;
		cin >> s >> n;
		for( int i = 0; i < s.length(); i++ ){
			string tmp;
			int cnt = 0, mx = 0;
			for( int j = i; j < s.length(); j++ ){
				tmp += s[j];
				if( isV( s[j] ) )
					cnt++;
				else cnt = 0;
				mx = max( mx, cnt );
				if( mx >= n ){
					res++;
				}
			}
		}
		cout << "Case #" << T++ << ": " << res << endl;
	}
	return 0;
}