# include <bits/stdc++.h>

#define sz size
#define pb push_back
#define fi first
#define se second
#define ppb pop_back
#define ln length
#define All(v) v.begin(),v.end()
#define mp make_pair

#define lld long long
#define str string
#define ulld unsigned long long
#define uld unsigned int
#define vv(x) vector < vector <x> >
#define ve(x) vector<x>

#define mod 1000000007

using namespace std;

ifstream fin( "file.in" );
ofstream fout( "file.out" );

int t,s;
string sl;

int main(){
	
	fin >> t;
	for( int i=0; i<t; i++ ){
		fin >> s >> sl;
		uld res=0,pn=0;
		for ( uld h=0; h<sl.length(); h++ ){
			if ( pn >= h )	pn+=(int)sl[h]-48;
			else res+=(h-pn),pn=h,pn+=(int)sl[h]-48;
		}
		
		fout << "Case #" << i+1 << ": " << res << '\n';
	}
	
	return 0;
}
