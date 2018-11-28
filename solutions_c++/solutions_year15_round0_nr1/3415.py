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
	string s;

	int l;
	int r,cur, d;
	forn(t,T) {
		cin>>l>>s;
		cur = 0;

		r=0;
		forn(i,l+1) {
			d = s[i]-'0';

			if (i==0) {
				cur = d;
			} else {
				if (i>cur) {
					r += i-cur;
					cur = i;
				}

				cur += d;
			}
		}

		cout<<"Case #"<<(t+1)<<": "<<r<<'\n';
	}
}