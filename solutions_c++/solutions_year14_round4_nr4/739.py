#include<iostream>
using namespace std;
int pow(int a,int b) {
	if(b==0 ) return 1;
	ll t = pow(a,b/2);
	if(b%2==1) return t*t*a;else return t*t;
}
int main()
{
	int T; cin>>T;
	while (T-- ) {
		int n,m;cin>>m>>n;
		for(int i=1;i<=m;i++){
			cin>>s[i];
		}
		for(int i=0;i<=pow(n,m)-1;i++){
			for(int j=0;j<n;j++){
				for(int i=0;i<s[i].length();i++) {
				
					S[j].insert(s[i].substr(0,i+1));
					
					cout<<s[i].substr(0,i+1)<<endl;
					
				}
			}
		}
		int tot=0;
		for(int i=0;i<n;i++){
			tot+=S[i].count();
		}
	}
	return 0;
}