#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <vector>
#include <bitset>
#include <string>
#include <ctype.h>
#include <stdio.h>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <float.h>
using namespace std;

#define oo 1e9
#define mp make_pair
#define pb push_back
#define bg puts("bug")
#define cl(A) A.clear()
#define pii pair<int,int>
#define sz(A) int(A.size())
#define rsz(A,B) A.resize(B)
#define ALL(A) A.begin(),A.end()
#define mem(A,B) memset(A,B,sizeof A)
#define rep(A,B,C) for(int A=B;A<C;A++)
#define rep_(A,B,C) for(int A=B;A>=C;A--)
//#define print(A) printf("%s = %d\n",#A,A)

typedef long long int lli;
typedef set<pii> ::iterator itS;
typedef unsigned long long int llu;
typedef map<int,int> ::iterator itM;

int dx[] = {0,0,1,-1,1,-1,1,-1} , dy[] = {1,-1,0,0,1,-1,-1,1};

int geti(){
	int y = 0, s = 1;
	char c = getchar();
	while ( !isdigit(c) && c!='-' ) c = getchar();
	if ( c == '-' ) s = -1 , c = getchar();
	while ( isdigit(c) ) y = y * 10 + ( c - '0' ) , c = getchar();
	return s * y;
}

llu setBit1 ( llu msk , llu idx ){ return msk | ( 1 << idx ); }
llu setBit0 ( llu msk , llu idx ){ return msk & ~( 1 << idx ); }
llu getBit  ( llu msk , llu idx ){ return ( ( msk >> idx ) & 1 ) == 1; }

int def ( const vector<double> & n , const vector<double> & k );
int war ( const vector<double> & n , const vector<double> & k );

int main (){

	/*
#ifndef ONLINE_JUDGE
	freopen("D-large.in", "rt", stdin);
	freopen("print.txt", "wt", stdout);
#endif
	*/

	int t = geti();

	rep ( a , 1 , t + 1 ){

		int n = geti();
		vector<double> N(n) , K(n);
		
		rep ( a , 0 , n ) cin >> N[a];
		rep ( a , 0 , n ) cin >> K[a];

		sort ( ALL ( N ) );
		sort ( ALL ( K ) );

		printf("Case #%i: %i %i\n",a, war ( N , K ),def ( N , K ));
	}

	return 0;
}

int war ( const vector<double> & n , const vector<double> & k ){

	int res = 0;
	bitset<1002> bs;
	bs.set();

	rep ( a , 0 , sz(n) ) rep ( b , 0 , sz(k) ) if ( n[a] > k[b] && bs[b] ){

		res++;
		bs[b] = 0;
		break;
	}

	return res;
}

int def ( const vector<double> & n , const vector<double> & k ){

	int res = 0;
	bitset<1002> bs;
	bs.set();

	rep_ ( a , sz(n) - 1 , 0 ){

		bool f = 1;
		rep ( b , 0 , sz(k) ) if ( k[b] > n[a] && bs[b] ) { 
			
			f = 0; 
			bs[b] = 0;		
			break; 
		}
		if ( f ) res++;
	}
	
	return res;
}