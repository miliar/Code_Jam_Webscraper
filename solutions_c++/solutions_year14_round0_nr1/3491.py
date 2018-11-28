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

int r[2];
int t[2][4][4];
int times[17];

int main(){
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		cout << "Case #" << tc << ": ";
		forn(k,2){
			cin >> r[k];
			r[k]--;
			forn(i,4)
				forn(j,4)
					cin >> t[k][i][j];
		}
		vector<int> res;
		forn(i,17)
			times[i] = 0;
		forn(k,2)
			forn(i,4)
				times[t[k][r[k]][i]]++;
		forn(i,17)
			if(times[i] >= 2)
				res.pb(i);
		if(res.size() == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else if(res.size() == 1){
			cout << res[0] << endl;
		}
		else if(res.size() >= 2){
			cout << "Bad magician!" << endl;
		}
	}
    return 0;
}
