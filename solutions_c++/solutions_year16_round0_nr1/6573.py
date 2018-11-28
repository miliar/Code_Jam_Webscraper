#include <bits/stdc++.h>
using namespace std;
int t, cnt;
long long n;
int x[10];
void solve(long long p) {
	int q;
	while(p) {
		q = p%10;
		if(x[q] == 0) {
			cnt++;
			x[q] = 1;
		}
		p /= 10;
	}
}
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("I.in","r",stdin);
		freopen("O.out","w",stdout);
	#endif
	cin>>t;
	for(int casen = 1; casen <= t; casen++) {
		cin>>n;
		cout<<"Case #"<<casen<<": ";
		if(n == 0) {
			cout<<"INSOMNIA"<<'\n';
			continue;
		}
		cnt = 0;
		memset(x,0,sizeof(x));
		for(int i=1;;i++) {
			solve(n*i);
			if(cnt == 10) {
				cout<<n*i<<'\n';
				break;
			}
		}
	}
	return 0;
}