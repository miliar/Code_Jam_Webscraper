/*
 * FirstProblem.cpp
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

int main() {
	freopen("test.txt", "rt", stdin);
	freopen("o.txt", "wt", stdout);

	int test;
	cin >> test;
	vector <string> XO;

	for(int U = 1; U <= test; U++ )
	{
		XO.clear();
		int resultRow[4]= {0,0,0,0};
		int resultCol[4]= {0,0,0,0};
		int d1 = 0 , d2 = 0;

		FOR(i,0,4)
		{
			string temp;
			cin>> temp;
			XO.pb(temp);
		}
		FOR(i,0,4)
		{
			//	cout << XO[i] << endl;
		}

		for(int i = 0; i < 4; i++)
		{
			//cout << "before"<< resultRow [i]<< endl;
			for(int x = 0; x < 4; x++ )
			{
				if(XO[i][x] == '.')
				{
					resultRow[i] = 0;
					break;
				}
				else if(XO[i][x] == 'X')
				{
					resultRow[i]+=10;
				}
				else if(XO[i][x] == 'O')
				{
					resultRow[i]+=1;
				}
				else if(XO[i][x] == 'T')
				{
					resultRow[i]+=2;
				}

			}
			//	cout << "after"<< resultRow [i]<< endl;
		}
		for(int x = 0; x < 4; x++ )
		{
			for(int i = 0; i < 4; i++)
			{
				if(XO[i][x] == '.')
				{
					resultCol[x] = 0;
					break;
				}
				else if(XO[i][x] == 'X')
				{
					resultCol[x]+=10;
				}
				else if(XO[i][x] == 'O')
				{
					resultCol[x]+=1;
				}
				else if(XO[i][x] == 'T')
				{
					resultCol[x]+=2;
				}

			}
		}
		for(int i = 0; i < 4; i++)
		{
			if(XO[i][i] == '.')
			{
				d1 = 0;
				break;
			}
			else if(XO[i][i] == 'X')
			{
				d1 +=10;
			}
			else if(XO[i][i] == 'O')
			{
				d1+=1;
			}
			else if(XO[i][i] == 'T')
			{
				d1+=2;
			}

		}
		for(int i = 0; i < 4; i++)
		{
			int x = 3-i;
			if(XO[i][x] == '.')
			{
				d2 = 0;
				break;
			}
			else if(XO[i][x] == 'X')
			{
				d2 +=10;
			}
			else if(XO[i][x] == 'O')
			{
				d2+=1;
			}
			else if(XO[i][x] == 'T')
			{
				d2+=2;
			}

		}
		bool result = false;
		if(result == false) {
			for(int i = 0; i < 4; i++)
			{
				if(resultCol[i] == 4 || resultCol[i] == 5 || resultRow[i] == 4 || resultRow[i] == 5 || d1 == 5||
						d1 == 4||d2 == 5||d2 == 4) {
					cout << "Case #" <<U <<": " << "O won" << endl;
					result = true;
					break;
				}
				else if (resultCol[i] > 31 || resultRow[i] > 31 ||d1 > 31||
						d1 > 31|| d2 >31||d2 > 31) {
					cout << "Case #" <<U <<": " << "X won" << endl;
					result = true;
					break;
				}
			}
		}
		if(result== false)
		{
			for(int i = 0; i < 4; i++)
			{
				if(resultCol[i] == 0 ||resultRow[i] == 0 ){
				cout << "Case #" << U <<": " << "Game has not completed" << endl;
				result = true;
				break;
				}
			}
		}
		if(result==false)
		{
			cout << "Case #" << U <<": " << "Draw" << endl;
		}

	}

	return 0;
}

