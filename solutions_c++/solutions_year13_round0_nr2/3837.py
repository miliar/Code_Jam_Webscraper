/*
 * Lawnmower
 * Apr 13, 2013,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <climits>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)
#define MOD(a,b) ((((a)%(b))+(b))%(b))
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int g[101][101];
int n, m;

bool ok() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int h = g[i][j];
			bool done = true;
			// try row
			for (int k = 0; k < m; k++)
				if (h < g[i][k]) {
					done = false;
					break;
				}
			if (done)
				continue;

			done = true;
			// try column
			for (int k = 0; k < n; k++)
				if (h < g[k][j]) {
					done = false;
					break;
				}
			if (!done)
				return false;

		}
	}
	return true;
}
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	cin>>t;
	loop2(id,1,t+1)
	{
		cin>>n>>m;
		loop(i,n) loop(j,m) cin>>g[i][j];
		cout << "Case #" << id << ": ";
		if(ok()) cout<<"YES";
		else cout<<"NO";
		cout<<endl;
	}
	return 0;
}
