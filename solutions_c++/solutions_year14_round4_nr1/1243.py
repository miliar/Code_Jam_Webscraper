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
#define filename "input"

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

int test = 1;
int n,w;
int a[111111];
bool used[111111];
int f[111111];
int fs(int pos){
	int res = 0;
	for (int i = pos; i > 0; i = (i & (i + 1)) -1) res += f[i];
	return res;
}

void md(int pos, int val){
	for (int i = pos; i <= n; i |= (i+1)) f[i] += val;
}

int find_(int val){
	int l = 1; int r = n;
	while (r - l > 1)
	{
		int c = (r + l ) / 2;
		if (a[c] <= val) r = c; else l = c;
	}
	if (a[l] <= val) return l;
	return r;
}

void solve(){
	cin >> n >> w;
	forab(i,1,n) cin >> a[i];
	forab(i,1,n)f[i] = 0;
	forab(i,1,n) used[i] = false;
	int ans = 0;
	sort(a + 1,a + n + 1);
	reverse(a + 1,a + n + 1);
	forab(i,1,n) if (!used[i]){
		int val = w - a[i];
		int pos = max(i+1, find_(val));
		if (pos <= n && a[pos] + a[i] <= w){
			int l = pos; int r = n;		
			while (r - l > 1){
				int c = (r + l) / 2;
				if (fs(c) - fs(pos -  1) != c - pos + 1) r = c; else l = c;
			}
			if (fs(l) - fs(pos - 1) != l - pos + 1){md(l,1); used[l] = true;} else
			if (fs(r) - fs(pos - 1) != r - pos + 1){md(r,1); used[r] = true;}
		}
		md(i, 1);
		used[i] = true;
		ans++;
	}
	cout << ans << endl;
}

int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);
	ios_base :: sync_with_stdio(false);
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
