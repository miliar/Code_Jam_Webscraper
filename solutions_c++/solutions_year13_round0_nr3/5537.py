/*
 * SecondProblem.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: mohammed
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 2e9
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
bool isPrim(ll x)
{
	if(x == 2) return true ;
	if(x < 2 || x % 2 == 0 ) return false ;
	for(int i = 3 ; i*i < x ; i+=2 )
	{
		if(x%i == 0)
			return false ;
	}
	return true;
}
bool isplandrom(ll x)
{
	stringstream ss  ;
	ss.str("");
	ss<< x ;
	string temp = ss.str();
	for(int i = 0 ; i <temp.size()/2 ;i++)
	{
		int u = temp.size()-1-i;
		if(temp[i] != temp[u])
			return false;
	}
	return true;
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	int test ;
	cin >> test ;
	for(int i =1 ; i <= test ; i++)
	{
		ll l , u ;
		cin >> l >> u ;
		int count = 0 ;
		for(ll h = l ; h <= u ; h++)
		{
			if(isplandrom(h))
			{
				//cout << h << endl;
				double long sqrtNumber = sqrt(h);
				//cout << sqrtNumber << endl;

				//if(sqrtNumber % 2 == 0 || sqrtNumber % 3 == 0)
				if(fabs(sqrtNumber) ==  (ll)sqrtNumber)
				if(isplandrom(sqrtNumber))
				{
					count++;
				}
			}
		}
		cout << "Case #"<<i<<": " << count << endl;
	}
	return 0;
}




