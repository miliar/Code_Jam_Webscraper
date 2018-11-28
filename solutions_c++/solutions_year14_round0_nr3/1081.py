#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <stack>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair
#define filename "in"

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

bool have[6][6][26];
vector <string> ans[6][6][26];
bool used[6][6];
int a[6][6];
int n,m;

void dfs(int x, int y){
	if (x < 0 || x >= n || y < 0 || y >= m)
		return;
	if (used[x][y])
		return;
	used[x][y] = true;
	int sum = 0;
	for (int i = -1; i < 2; i++)
		for (int j = -1; j < 2; j++)
			if (x + i< 0 || x +i >= n || y +j < 0 || y+j >= m) continue; else
				sum += a[x+i][y+j];
	if (sum == 0){
		for (int i = -1; i < 2; i++)
			for (int j = -1; j < 2; j++)
				dfs(x+i,y+j);
		
	}
}

void solve(){
	cout << endl;
	int t,g,b;
	cin >> t >> g >> b;
	if (!have[t][g][b])
		cout << "Impossible\n";
	else{
		foru(q,ans[t][g][b].size()) cout << ans[t][g][b][q] << endl;
	}
}

const int nmax = 5;

int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);
	
	for (n = 1; n <= nmax; n++)
		for (m = 1; m <= nmax; m++){
			int l = 1 << (n*m);
			for (int i = 0; i < l; i++){
				int x = i;
				int kol = 0;
				while (x > 0){
					x &= (x-1);
					kol++;
				}
				if (have[n][m][kol]) continue;
				for (int j = 0; j < n*m; j++)
					a[j / m][j % m] = (i & (1 << j)) > 0;
				foru(q,n) foru(w,m) if (a[q][w] == 0){
					if (have[n][m][kol]) break;
					foru(o,n) foru(r,m) used[o][r] = false;
					dfs(q,w);
					bool tmp = true;
					foru(o,n) foru(r,m){
						if (a[o][r] == 0 && !used[o][r]){
							tmp = false;
							break;
						}
					}
					if (tmp){
						have[n][m][kol] = true;
						foru(o,n){
							string s ="";
							foru(r,m) if (a[o][r] == 1) s += '*'; else
							if (o == q && r == w) s += 'c'; else s += '.';
							ans[n][m][kol].pb(s);
						}
					}
						
				}
			}
		}

	/*for (n = 1; n <= nmax; n++) for (m = 1; m <= nmax; m++) for (int kol = 0; kol < n*m; kol++){
		if (!have[n][m][kol]){
			cout << n << " " << m << " " << kol << " " << 0 << endl;		
		} else{
			cout << n << " " << m << " " << kol << " " << 1 << endl;
			foru(j,ans[n][m][kol].size()) cout << ans[n][m][kol][j] << endl;
		}
	}*/
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": "; solve();
	}
	return 0;
}
