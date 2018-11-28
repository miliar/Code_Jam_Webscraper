#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include <deque>
#include<ctime>
using namespace std;
typedef long long ll;
int cnt[2510];
void useFile(const string &name) {
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
}
void deal() {
	memset(cnt,0,sizeof(cnt));
	int n,x,l;
	cin>>n;
	l = n*2-1;
	for(int i=0;i<l;++i) {
		for(int j=0;j<n;++j) {
			cin>>x;
			++cnt[x];
		}
	}
	int outcnt = 0;
	for(int i=1;i<=2500;++i) {
		if(cnt[i]&1) {
			if(outcnt)
				cout<<' ';
			cout<<i;
			++outcnt;
		}
	}
	cout<<endl;
}
int main() {
	int n;
	useFile("B-large");
	cin>>n;
	for(int i=1;i<=n;++i){
		cout<<"Case #"<<i<<": ";
		deal();
	}
	return 0;
}
