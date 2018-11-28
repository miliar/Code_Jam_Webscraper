#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>
#include <time.h>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB; 
typedef vector<VI> VVI;
const long double pi = 3.14159265358979323846;
const int inf = (int)1e9;

const LL base=inf;

bool pred (const string& i, const string& j)
{
    return i.size()<j.size();
}

int x[2][4][4];

int main(){
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
   // freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif  
	int t;
	cin >> t;
	FOR(tt,t) {
		cout << "Case #" << tt + 1 << ": ";
		VI a(2);
		FOR(qq,2) {
			cin >> a[qq];
			--a[qq];
			FOR(i,4) {
				FOR(j,4) {
					cin >> x[qq][i][j];
				}
			}
		}
		VI ans;
		map<int,int> m;
		FOR(i,4) {
			m[x[0][a[0]][i]]++;
			m[x[1][a[1]][i]]++;
		}
		for(map<int,int>::iterator it = m.begin(); it != m.end(); ++it) {
			if (it->second > 1) {
				ans.pb(it->first);
			}
		}
		if (ans.size() == 0) {
			cout << "Volunteer cheated!\n";
		}
		if (ans.size() == 1) {
			cout << ans[0] << "\n";
		}
		if (ans.size() > 1) {
			cout << "Bad magician!\n";
		}
	}
    return 0;
}