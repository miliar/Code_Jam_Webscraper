#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ft first
#define se second
#define mp make_pair

int main(int argc, char const *argv[]){
	int T,p;
	cin>>T;
	p=T;
	while(T--){
		int n;
		cin>>n;
		int a[n];
		for (int i = 0; i < n; ++i){
			cin>>a[i];
		}
		int o=0;
		for (int i = 0; i < n-1; ++i){
			if(a[i+1]<a[i]) o+=abs(a[i+1]-a[i]);
		}
		int s=0;
		for (int i = 0; i < n-1; ++i){
			s=max(a[i]-a[i+1],s);
		}
		int t=0;
		for (int i = 0; i < n-1; ++i){
			if(a[i]>0) t+=min(s,a[i]);
		}
		cout<<"Case #"<<p-T<<": "<<o<<" "<<t<<endl;
	}
	return 0;
}