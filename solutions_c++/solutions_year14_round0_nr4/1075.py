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

double a[1111],b[11111];
int n;
bool used[1111];

void solve(){
	cin >> n;
	foru(i,n) cin >> a[i];
	foru(i,n) cin >> b[i];
	sort(a,a+n);
	sort(b,b+n);
	foru(i,n) used[i] = false;
	int kol2 = 0;
	foru(i,n){
		int pos = -1;
		ford(j,n)
			if (b[j] > a[i] && !used[j]){
				pos = j;				
			}
		if (pos == -1)
			ford(j,n) if (!used[j]) pos = j;
		used[pos] = true;
		if (a[i] > b[pos]) kol2++;
	}
	int kol1 = n;
	int pos = n-1;
	bool r = true;
	foru(i,n) if (a[i] < b[i]) r = false;
	if (!r){kol1 = 0;
	foru(i,n){
		int len = n - i - 1;
		bool fl = true;
		foru(j,len) if (a[i + j + 1] < b[j]) fl = false;
		if (fl){
			kol1 = len;
			break;		
		}
	}}
	cout << kol1 << " " << kol2 << endl;
}

int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": "; solve();
	}
	return 0;
}
