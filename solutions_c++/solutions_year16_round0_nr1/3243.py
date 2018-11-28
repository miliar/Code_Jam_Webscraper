#include <bits/stdc++.h>
using namespace std;
#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))
#define abs(x) ((x) < 0 ? -(x) : (x))


int t;
long long inp,num,tar;
bool f[10];
int lft;

void clc(long long n) {
	int m;
	while (n>0) {
		m=n%10;
		if (!f[m]) {
			--lft; f[m]=true;
		}
		n/=10;
	}
}

int main()
{
	cin.sync_with_stdio(0);
	//cin.tie(0);
	cin >> t;
	for (int tcs=1;tcs<=t;++tcs) {
		cin >> inp;
		if (inp==0) { cout << "Case #" << tcs << ": INSOMNIA\n"; continue; }
		if (inp==1000000) { cout << "Case #" << tcs << ": 9000000\n"; continue; }
		lft=10; for (int i=0;i<10;++i) f[i]=false;
		num=inp;
		while (true) {
			clc(num);
			if (lft==0) break;
			num+=inp;
		}
		cout << "Case #" << tcs << ": " << num << "\n"; continue;
	}
	return 0;
}

