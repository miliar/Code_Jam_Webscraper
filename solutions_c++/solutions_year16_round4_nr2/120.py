#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

ld dp[222][222];

ld check(vector<ld> t){
	for (int i=0;i<=(int)t.size();i++){
		for (int ii=0;ii<=(int)t.size();ii++){
			dp[i][ii]=0;
		}
	}
	dp[0][0]=1;
	for (int i=0;i<(int)t.size();i++){
		for (int ii=0;ii<(int)t.size();ii++){
			dp[i+1][ii+1]+=dp[i][ii]*t[i];
			dp[i+1][ii]+=dp[i][ii]*((ld)1-t[i]);
		}
	}
	return dp[(int)t.size()][(int)t.size()/2];
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		int n,k;
		cin>>n>>k;
		vector<ld> p(n);
		for (int i=0;i<n;i++){
			cin>>p[i];
		}
		sort(p.begin(), p.end());
		ld v=0;
		for (int a=0;a<=k;a++){
			vector<ld> t;
			for (int j=0;j<a;j++){
				t.push_back(p[j]);
			}
			for (int j=n-k+a;j<n;j++){
				t.push_back(p[j]);
			}
			assert((int)t.size()==k);
			v=max(v, check(t));
		}
		cout<<setprecision(15)<<v<<endl;
	}
}