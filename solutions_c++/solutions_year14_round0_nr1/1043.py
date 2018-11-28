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

const int n = 4;
int a[n],b[n];

void solve(){
	int p1;
	int x;
	cin >> p1; p1--;
	foru(i,n) foru(j,n){
		cin >> x;
		if (i == p1) a[j] = x;	
	}
	cin >> p1; p1--;
	foru(i,n) foru(j,n){
		cin >> x;
		if (i == p1) b[j] = x;	
	}
	int kol = 0;
	foru(i,n) foru(j,n)	if (a[i] == b[j]) kol++;
	switch (kol) {
		case 0 : {
			cout << "Volunteer cheated!";
			break;
		}
		case 1 : {
			foru(i,n) foru(j,n) if (a[i] == b[j]) x = a[i];
			cout << x; 
			break;
		}
		default : {
			cout << "Bad magician!";
		}
	}
	cout << endl;	
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
