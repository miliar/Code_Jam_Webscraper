#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <deque>
#include <string>
#include <cstring>
#include <fstream>
#include <iostream>

#define _USE_MATH_DEFINES
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#define LL long long
using namespace std;

#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define mp make_pair
#define sqr(x) x*x
#define LL long long 

void smain();
int main() {
	ios_base::sync_with_stdio(false);

#ifdef _DEBUG
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);
#endif

	smain();

	return 0;
}

#define int long long

void smain() {
	int T;
	cin>>T;
	forn(t,T) {
		int d;
		cin>>d;
		vector <int> a(d);

		int mm=0, res, maxres=-1, b;
		forn(i,d) {
			cin>>a[i];
			mm = max(mm,a[i]);
		}

		maxres = mm;
		for (int tt=1;tt<=mm;tt++) {
			res = tt;
			forn(i,d) {
				b = a[i]/tt;
				if (a[i]%tt)
					b++;

				res += b-1;
			}

			if (maxres >res)
				maxres = res;
		}

		cout<<"Case #"<<(t+1)<<": "<<maxres<<'\n';
	}
}