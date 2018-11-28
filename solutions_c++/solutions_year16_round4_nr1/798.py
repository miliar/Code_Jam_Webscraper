#include <bits/stdc++.h>
using namespace std;
typedef double lf;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;
typedef pair<ll, ll> pll;
#define pb push_back
#define SZ(x) ((int)(x).size())
inline int ri() {
	int x=0, f=1, c=getchar();
	for(; c<48||c>57; f=c=='-'?-1:f, c=getchar());
	for(; c>47&&c<58; x=x*10+c-48, c=getchar());
	return x*f;
}
int n, A, B, C, a, b, c;
string cal(int x, int y) {
	if(!x) {
		if(y==0) {
			++a;
			return "R";
		}
		else if(y==1) {
			++b;
			return "P";
		}
		else {
			++c;
			return "S";
		}
	}
	if(y==0) {
		string l=cal(x-1, y), r=cal(x-1, 2);
		if(l>r) {
			swap(l, r);
		}
		return l+r;
	}
	else if(y==1) {
		string l=cal(x-1, y), r=cal(x-1, 0);
		if(l>r) {
			swap(l, r);
		}
		return l+r;
	}
	else {
		string l=cal(x-1, y), r=cal(x-1, 1);
		if(l>r) {
			swap(l, r);
		}
		return l+r;
	}
	return "";
}
int main() {
	for(int _=1, T=ri(); _<=T; ++_) {
		printf("Case #%d: ", _);
		n=ri();
		A=ri();
		B=ri();
		C=ri();
		string ans="";
		a=b=c=0;
		string t=cal(n, 0);
		if(a==A && b==B && c==C) {
			if(ans=="") {
				ans=t;
			}
			else {
				ans=min(ans, t);
			}
		}
		a=b=c=0;
		t=cal(n, 1);
		if(a==A && b==B && c==C) {
			if(ans=="") {
				ans=t;
			}
			else {
				ans=min(ans, t);
			}
		}
		a=b=c=0;
		t=cal(n, 2);
		if(a==A && b==B && c==C) {
			if(ans=="") {
				ans=t;
			}
			else {
				ans=min(ans, t);
			}
		}
		if(ans=="") {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%s\n", ans.c_str());
		}
	}
	return 0;
}
