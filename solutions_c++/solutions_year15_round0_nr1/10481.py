#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
#include<string>
#include<utility>
#include<bitset>
#include<cctype>
#include<cstring>

using namespace std;


int main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int t=0,in=1;
	for(cin>>t;t--;){
		int smax,invite=0;
		cin>>smax;
		
		char s[smax+2],aud=0;
		for(int i=0;i<smax+1;i++){
		cin>>s[i];
		
		if(s[i]-'0'>0){
			if(i>aud) {
			invite+=(i-aud);
			aud+=invite;
			}
		}
	aud+=s[i]-'0';
	}
		
	cout<<"Case #"<<in++<<": "<<invite<<endl;
	}
return 0;
}
