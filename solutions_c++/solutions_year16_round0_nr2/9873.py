#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef long long ll;

map<string, int> dp;

int vv=10000;

int n;

void go(string b, int v){
	int f=0;
	for (int i=0;i<n;i++){
		if (b[i]=='-') f=1;
	}
	if (f==0) vv=min(vv, v);
	if (dp[b]>0){
		if (dp[b]<=v) return;
	}
	dp[b]=v;
	for (int i=0;i<n;i++){
		string lol;
		for (int j=0;j<=i;j++){
			if (b[j]=='-') lol+='+';
			else lol+='-';
		}
		reverse(lol.begin(), lol.end());
		for (int j=i+1;j<n;j++){
			lol+=b[j];
		}
		go(lol, v+1);
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		string s;
		cin>>s;
		n=s.size();
		vv=100000;
		dp.clear();
		go(s, 1);
		cout<<vv-1<<endl;
	}
}