#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,i,j;string s;
	cin>>T;
	for(i=1;i<=T;++i){
		printf("Case #%d: ",i);
		cin>>s;
		string ret;
		for(j=0;j<s.size();++j){
			if(j==0)ret+=s[j];
			else{
				if(ret[0]<=s[j])
					ret = s[j]+ret;
				else
					ret+=s[j];
			}
		}
		cout<<ret<<endl;
	}
}
