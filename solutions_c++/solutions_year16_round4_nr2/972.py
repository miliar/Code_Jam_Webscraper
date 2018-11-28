#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define F first
#define S second
#define maxn 100005
#define mod 1000000007

int main(){
	ios::sync_with_stdio(false);
	
	int t;
	cin>>t;

	for(int tc=1;tc<=t;tc++){
		cout<<"Case #"<<tc<<": ";
		int n,k;
		cin>>n>>k;
		long double a[n];
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		sort(a,a+n);
		double ynny;
		double eq=1;
		double yy;
		double nn;
		double py;
		double pn;
		for(int i=0;i<k/2;i++){
			ynny=a[i]*(1-a[n-i-1])+a[n-i-1]*(1-a[i]);
			eq=eq*ynny;
			yy=a[i]*a[n-i-1];
			nn=(1-a[n-i-1])*(1-a[i]);
			if(i==0){
				py=yy;
				pn=nn;
				continue;
			}
			eq+=py*nn+pn*yy;
			py*=ynny;
			pn*=ynny;
		}
		cout<<fixed<<setprecision(7)<<eq<<endl;
	}

	return 0;
}