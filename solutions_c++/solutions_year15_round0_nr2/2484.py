#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

inline int min(int a, int b) { return a<b?a:b; }
inline int max(int a, int b) { return a>b?a:b; }

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin>>T;

	for(int t=1 ; t<=T ; t++) {	
		int D, ans=0;
		cin>>D;

		vector<int> P(D);
		for(int i=0 ; i<D ; i++) { cin>>P[i]; ans=max(ans,P[i]); }

		for(int i=1 ; i<=1000 ; i++) {
			int ans2=0;
			for(int j=0 ; j<D ; j++) {
				if(P[j]>i) ans2 += ((P[j]%i==0)?(P[j]/i-1):(P[j]/i));
			}
			
			ans=min(ans,ans2+i);
		}

		cout<<"Case #"<<t<<": ";
		cout<<ans<<"\n";
	}

	return 0;
}