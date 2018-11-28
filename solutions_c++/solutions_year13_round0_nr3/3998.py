#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int maxn=10000000;
long long a,b;
int fair[100000],n;

bool check(int num) {
	int t1=num,t2=0;
	while (t1) {
		t2=t2*10+t1%10;
		t1/=10;
	}
	return num==t2;
}

bool check2(long long num) {
	long long t1=num,t2=0;
	while (t1) {
		t2=t2*10+t1%10;
		t1/=10;
	}
	return num==t2;
}

void init() {
	n=0;
	for (int i=1;i<maxn;i++)
		if (check(i))
			fair[n++]=i;
}

void solve() {
	int i;
	long long t;
	for (i=0;i<n;i++) {
		t=fair[i];
		t=t*t;
		if (t>=a)
			break;
	}

	int ans=0;
	for (;i<n;i++) {
		t=fair[i];
		t=t*t;
		if (t>b) break;
		if (check2(t)) ans++;
	}
	cout<<ans<<endl;
}

int main() {
	init();
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>a>>b;
		cout<<"Case #"<<++kase<<": ";
		solve();
	}
	return 0;				
}

