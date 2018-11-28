/*
 * D.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Mostafa Saad
 */



#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)

typedef long long         ll;


const double EPS = (1e-7);
int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}

#define pb					push_back
#define MP					make_pair
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
typedef long double   	  ld;
typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;

vector< vector<int> > boxesKeys;
vector<int> unlockBoxesKey;
int K, N;
vector<int> sol;
bool found;

void add(vector<int> &myKeys, vector<int> &keysList, int sign)
{
	rep(i, keysList)
		myKeys[ keysList[i] ] += sign;
}
typedef bitset<20> MASK;

bool worth(vector<int> myKeys, MASK boxesStatus)
{
	bool change = 1;

	while(change)
	{
		change = 0;
		lp(i, N) if(!boxesStatus[i] && myKeys[ unlockBoxesKey[i] ]) {
			boxesStatus[i] = 1;
			change = 1;
			add(myKeys, boxesKeys[i], 1);
		}
	}

	lp(i, N) if(!boxesStatus[i])
		return false;

	return 1;
}



typedef pair<vector<int>, int> ENTRY;

map<ENTRY, bool> mp;

bool go(vector<int> &myKeys, MASK& boxesStatus)
{
	if(sz(sol) == N)
		return 1;

	ENTRY pp = make_pair(myKeys, boxesStatus.to_ulong());

	if(mp.count(pp))
		return mp[pp];

	if(!worth(myKeys, boxesStatus) )
		return mp[pp];

	lp(i, N) if(!boxesStatus[i] && myKeys[ unlockBoxesKey[i] ]) {
		--myKeys[ unlockBoxesKey[i] ];
		boxesStatus[i] = 1;
		add(myKeys, boxesKeys[i], 1);

		sol.push_back(i);

		if( go(myKeys, boxesStatus) )
			return mp[pp] = 1;

		sol.pop_back();
		add(myKeys, boxesKeys[i], -1);
		boxesStatus[i] = 0;
		++myKeys[ unlockBoxesKey[i] ];
	}

	return mp[pp] = 0;
}

int idx(vector<int> &v, int val)
{
	return find(all(v), val) - v.begin();
}

int main()
{
	freopen("D-small-attempt1.in", "rt", stdin);
	freopen("D-small-attempt1.out.txt", "wt", stdout);

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		mp.clear();
		boxesKeys.clear();
		unlockBoxesKey.clear();
		sol.clear();
		found = false;

		cin>>K>>N;

		set<int> keySet;

		vector<int> myTempKeys;
		lp(i, K) {
			int k;
			cin>>k;
			myTempKeys.push_back(k);
			keySet.insert(k);
		}

		boxesKeys = vector< vector<int> > (N);
		unlockBoxesKey = vector<int>(N);
		lp(i, N)
		{
			int k;
			cin>>unlockBoxesKey[i]>>k;
			keySet.insert( unlockBoxesKey[i] );

			lp(j, k)
			{
				int op;
				cin>>op;
				boxesKeys[i].push_back(op);
				keySet.insert(op);
			}
		}

		vector<int> keysVec( all(keySet) );
		vector<int> myKeys( sz(keysVec) );
		rep(i, myTempKeys)
			myKeys[ idx(keysVec, myTempKeys[i]) ]++;

		lp(i, N)
		{
			unlockBoxesKey[i] = idx(keysVec,unlockBoxesKey[i]);

			rep(j, boxesKeys[i])
			 	boxesKeys[i][j] = idx(keysVec, boxesKeys[i][j]);
		}

		MASK boxesStatus;

		if ( go(myKeys, boxesStatus) )
		{
			cout<<"Case #"<<cc+1<<":";
			rep(i, sol)
				cout<<" "<<sol[i]+1;
			cout<<"\n";
		}
		else
			cout<<"Case #"<<cc+1<<": IMPOSSIBLE\n";

		cout<<flush;

	}




	return 0;
}
