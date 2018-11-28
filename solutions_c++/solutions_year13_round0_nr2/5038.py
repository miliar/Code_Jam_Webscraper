#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define pb push_back
#define x first
#define y second


using namespace std;


int main()
{
	int t,n,m;
	int desired[110][110];
	int act[110][110];
	int maxr[110];
	int maxc[110];

	cin >> t;
	forn(caso,t){
		cin >> n >> m;
		forn(i,n){ 
			maxr[i] = -1;
			forn(j,m) { 
				cin >> desired[i][j];
				act[i][j] = 100;
				maxr[i] = max(maxr[i],desired[i][j]);
			}
		}

		forn(j,m){
			maxc[j] = -1;
			forn(i,n){
				maxc[j] = max(maxc[j],desired[i][j]);
			}
		}

		forn(j,m)
			forn(i,n) act[i][j] = min(act[i][j], maxc[j]);

		forn(i,n)
			forn(j,m) act[i][j] = min(act[i][j], maxr[i]);
		
		bool des = true;
		for(int i = 0; (i < n) and des; i++)
			for(int j = 0; (j < m) and des; j++){ des = (act[i][j] == desired[i][j]); }

		if(des)	cout << "Case #" << (caso+1) << ": " << "YES" << endl;
		else cout << "Case #" << (caso+1) << ": " << "NO" << endl;
	}
	return 0;		
}
