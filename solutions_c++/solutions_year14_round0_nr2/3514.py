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
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define formn(i,m,n) for(int i=m;i<(int)n;i++)
#define dformn(i,m,n) for(int i=n-1;i>=m;i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

double C,F,X;

int main(){
freopen("Blarge.in","r",stdin);
freopen("Blarge.out","w",stdout);
	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		cout << "Case #" << tc << ": ";
		cin >> C >> F >> X;
		double t = 0.0;
		tint f = 0;
		double res = X/2.0;
tint bestF = -1;
		while(((double)f) < X + 10.0){
			if(res > t + X/(2.0 + ((double)f) * F)){
				bestF = f;
			}
			res = min(res, t + X/(2.0 + ((double)f) * F));
			double delta = C/(2.0 + ((double)f) * F);
			t += delta;
			f++;
		}
cerr << bestF << " " << (int)(X/C - 2.0/F) << endl;
		cout << setprecision(7) << fixed << res << endl;
	}
    return 0;
}
