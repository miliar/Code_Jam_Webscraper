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
#define filename "inp"

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

int a[111][111];
set <string> q;
string s[111];
int ans, all;

void init(int n){
	q.clear();
	foru(i,n) foru(j,110) a[i][j] = 0;
	ans = 0;
	all = 0;
}

void solve(){
	int n;
	cin >> n;
	init(n);
	foru(i,n) cin >> s[i];
	foru(i,n){
		string u = "";
		u += s[i][0];
		forab(j,1,s[i].size()-1) if (s[i][j] != s[i][j-1]) u += s[i][j];
		q.insert(u);
	}
	if (q.size() > 1){
		cout << "Fegla Won";
		return;
	}
	foru(i,n){
		int pos = 0;
		a[i][pos]++;
		forab(j,1,s[i].size() - 1){
			if (s[i][j] != s[i][j-1]) pos++;
			a[i][pos]++;
		}
		all = pos + 1;
	}
//	cout << all << endl;
	foru(i,all){
		int tmp = 1000000000;
		forab(ret,1,100){
			int tu = 0;
			foru(j,n) tu += abs(a[j][i] - ret);
			tmp = min(tmp, tu);
		}
		ans += tmp;			
	}
	cout << ans;
}

int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);	
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		//cout << "----\n";
		cout << "Case #" << tt << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
