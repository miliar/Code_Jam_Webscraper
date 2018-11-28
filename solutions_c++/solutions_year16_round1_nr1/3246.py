#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int tc,cp=1; string s,s2;
	cin>>tc;
	while(tc--){
		cin>>s;
		s2=s[0];
		//cout<<"s2:"<<s2<<endl;
		for(int i=1;i<s.size();i++){
			if(s2[0]>s[i]){
				s2=s2+s[i];
			}else{
				s2=s[i]+s2;
			}
		}
		cout<<"Case #"<<cp++<<": "<<s2<<'\n';
	}
	return 0;
}
