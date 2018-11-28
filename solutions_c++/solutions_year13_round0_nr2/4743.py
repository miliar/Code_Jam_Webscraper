// Algorithm    :
// Order        :

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <list>
#include <complex>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef complex<double> point;

#define X real()
#define Y imag()
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define L(s) (int)((s).size())
#define C(a,b) memset((a),(b),sizeof(a))
#define all(c) (c).begin(), (c).end()

#define INF (1e15)
#define EPS (1e-9)

#define MAX 110
int n,m;
int a[MAX][MAX];

bool check(int I, int J) {
	int Max = a[I][J];
	bool p1 = 1, p2 = 1;
	for(int i=0;i<n;i++)
		if(a[i][J] > Max)
			p1 = 0;
	for(int j=0;j<m;j++)
		if(a[I][j] > Max)
			p2 = 0;
	return (p1|p2);
}

bool CHECK() {
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(!check(i,j))
				return 0;
	return 1;
}
int main () {
	int _te;
	cin >> _te;
	for(int te=1;te<=_te;te++) {
		cin >> n >> m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin >> a[i][j];
		cout << "Case #" << te << ": " << (CHECK()? "YES" : "NO") << endl;
	}
	return 0;
}







