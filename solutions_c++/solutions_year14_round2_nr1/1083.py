#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#define NAME "a-large"
#define sz(x) (int)(x).size()
using namespace std;
int T;
string s[200];
int j[200],l[200];
int main(){
	freopen(NAME".in","rt",stdin);
	freopen(NAME".out","wt",stdout);
	cin>>T;
	for(int I=1;I<=T;I++) {
		printf("Case #%d: ",I);
		int n,ans=0;
		cin>>n;
		for(int i=0;i<n;i++) {
			cin>>s[i];
			j[i]=0;
		}
		bool felgaWon=0;
		while(j[0]<sz(s[0])){
			char c=s[0][j[0]];
			for(int i=0;i<n;i++) {
				if(j[i]>=sz(s[i]) || s[i][j[i]]!=c) {
					felgaWon=1;
				} else {
					l[i]=0;
					while(j[i]<sz(s[i]) && s[i][j[i]]==c) {
						j[i]++;
						l[i]++;
					}
				}
			}
			int nans=10000000;
			for(int i=0;i<n;i++) {
				int nnans=0;
				for(int ii=0;ii<n;ii++) {
					nnans+=abs(l[i]-l[ii]);
				}
				nans=min(nans,nnans);
			}
			ans+=nans;
		}
		for(int i=0;i<n;i++) if(j[i]!=sz(s[i])) felgaWon=1;
		if(felgaWon) cout<<"Fegla Won\n";
		else cout<<ans<<'\n';
	}
	return 0;
}