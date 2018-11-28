#include <iostream>
#include <cstdio>
#define NAME "d-large"
using namespace std;
int T;
int main(){
	freopen(NAME".in","rt",stdin);
	freopen(NAME".out","wt",stdout);
	cin>>T;
	for(int I=1;I<=T;I++) {
		printf("Case #%d: ",I);
		int n;
		cin>>n;
		long double ken[1001],nao[1001];
		bool used[2001];
		for (int i=0;i<2*n;i++) {
			cin>>(i>=n?ken[i-n]:nao[i]);
			used[i]=0;
		}
		int y=0,z=n,mj;
		for(int i=0;i<n;i++) {
			for(int j=i+1;j<n;j++) {
				if(nao[i]>nao[j]) swap(nao[i],nao[j]);
				if(ken[i]>ken[j]) swap(ken[i],ken[j]);
			}
		}
		/*
		count z
		*/
		bool ok;
		int start=0;
		for(int i=0;i<n;i++) {
			ok=0;
			for(int j=start;j<n;j++) {
				if(!used[j] && ken[j]>nao[i]) {
					used[j]=1;
					z--;
					ok=1;
					break;
				}
			}
			if(!ok) {
				for(int j=start;j<n;j++) {
					if(!used[j]) {
						start=j+1;
						break;
					}
				}
			}
		}
		/*
		count y
		*/
		for(int i=0;i<n;i++) {
			ok=1;
			for(int j=i;j<n;j++) {
				if(ken[j-i]>nao[j]) ok=0;
			}
			if(ok) {
				y=n-i;
				break;
			}
		}
		cout<<y<<" "<<z<<endl;
	}
	return 0;
}