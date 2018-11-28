///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>
#include<assert.h>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0; i<(int)n; i++)
#define dforn(i,n) for(int i=(int)n-1; i>=0; i--)
#define formn(i,m,n) for(int i=m; i<(int)n; i++)
#define dformn(i,m,n) for(int i=n-1; i>=m; i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

int main(){
freopen("B.in","r",stdin);
freopen("B.out","w",stdout);
	int TC;
	cin >> TC;
	forn(tc,TC){
		int P;
		cin >> P;
		int a[P];
		forn(i, P)
			cin >> a[i];
		int res = 1000;
		for(int como = 1; como <= 1000; como++){
			int muevo = 0;
			forn(i, P)
				muevo += (a[i] - 1) / como;
			res = min(res, como + muevo);
		}
		cout << "Case #"<< tc + 1 << ": " << res << endl;
	}
    return 0;
}
