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
#define print(A) printf("%s = %d\n",#A,A)
#define fast ios_base::sync_with_stdio(false)

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

int main (){

#ifndef ONLINE_JUDGE
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("print.txt", "wt", stdout);
#endif

	int t = geti();

	rep ( a , 1 , t + 1 ){

		int q1 = geti();
		int g1[4][4];
		bitset<17> bs1;
		bs1.set();

		rep ( a , 0 , 4 ) rep ( b , 0 , 4 ){

			g1[a][b] = geti();
			if ( a == q1 - 1 ) bs1[g1[a][b]] = 0;
		}

		int q2 = geti();
		int g2[4][4];
		bitset<17> bs2;
		bs2.set();

		rep ( a , 0 , 4 ) rep ( b , 0 , 4 ){

			g2[a][b] = geti();
			if ( a == q2 - 1 ) bs2[g2[a][b]] = 0;
		}
		vector<int> v;
		rep ( a , 1 , 17 ) if ( !bs1[a] && !bs2[a] ) v.push_back(a);

		printf("Case #%i: ",a);
		if ( sz(v) == 0 )
			puts("Volunteer cheated!");
		else
			if ( sz(v) > 1 ) 
				puts("Bad magician!");
			else
				printf("%i\n",v[0]);
	}


	return 0;
}