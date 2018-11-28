// google-code-jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>



using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

#define LARGE

int N,nx;


int _tmain(int argc, _TCHAR* argv[])
{
#ifdef TEST
	freopen("./data/2013/C-small.in", "rt", stdin);
	freopen("./data/2013/C-small.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("./data/2013/C-small-attempt0.in", "rt", stdin);
	freopen("./data/2013/C-small-attempt0.out", "wt", stdout);
#endif

#ifdef LARGE
	freopen("./data/2013/C-large-1.in", "rt", stdin);
	freopen("./data/2013/C-large-1.out", "wt", stdout);
#endif
	ll allpals[5000];
	int w = 0;
	ll max_num = sqrt(1000000000000000);
	for (ll a=0;a<max_num;a++){
		char n_num[100];
		char a_num[100];
		memset(n_num,0,100);
		memset(a_num,0,100);
		bool palindrome_a = true;
		bool palindrome_n = true;
		// create square
		ll square = a*a;
		sprintf(n_num,"%lld",square);
		sprintf(a_num,"%lld",a);
		
		// check if it is palidrome a
		int pos = 0;
		while (pos < (strlen(a_num)/2)) {
			if (a_num[pos]!=a_num[strlen(a_num)-pos-1]) {
				palindrome_a = false;
				break;
			}
			pos++;
		}
		if (!palindrome_a){
			continue;
		}
		// check if it is palidrome N
		pos = 0;
		while (pos < (strlen(n_num)/2)) {
			if (n_num[pos]!=n_num[strlen(n_num)-pos-1]) {
				palindrome_n = false;
				break;
			}
			pos++;
		}

		if (palindrome_n) {
			allpals[w] = square;
			w++;
			//cout << "a=" << a_num << ";square = " << n_num << endl;
		}
	}

	cin >> N;
	for (int nn=1; nn<=N; nn++){
		cout << "Case #" << nn << ": ";
		ll interval_min = 0;
		ll interval_max = 1;
		int count_of_pals = 0;
		cin >> interval_min;
		cin >> interval_max;
		for (int f=0;f<(w-1);f++){
			if (allpals[f]<interval_min) {
				continue;
			}
			if (allpals[f]>interval_max) {
				break;
			}
			count_of_pals++;
		}
		cout << count_of_pals << endl;
	}
	return 0;
}

