#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#define N 101
#define ll long long

using namespace std;

int T;

int f[11111111];

int n,m;

long long a,b;

int chek(ll num){
	int kol=0;
	int a[100];
	while (num){
		a[kol++]=(num%10);
		num/=10;
	}
	for (int i=0;i<kol;i++) if (a[i]!=a[kol-i-1]) return 0;
	return 1;
}

int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	f[0]=0;
	int cc=0;
	int numbrs[1000],p=0;
	for (int x=1;x<10000001;x++) {
		f[x]=f[x-1]+(chek(x) && chek((ll)x*(ll)x));
		if (f[x]!=f[x-1]) numbrs[p++]=x;
	}
	while (T--){
		cin >> a >> b;
		int ans=0;
		for (int i=0;i<p;i++){
			ll x=(ll)numbrs[i]*(ll)numbrs[i];
			if ((x>=a) && (x<=b)) ans++;
		}
		cc++;
		cout << "Case #" << cc << ": " << ans << endl;
	}
	return 0;
}
