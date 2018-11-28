#include<bits/stdc++.h>
using namespace std;
int main(){
	string str;
	int ti,len,t,i,pos,ans,total;
	cin >> ti;
	for(t=1;t<=ti;++t){
		cin >> str;
		len = str.length();
		vector<char> aa;
		aa.push_back(str[0]);
		pos = 1;
		while(pos<len){
			while(pos < len && aa.back()==str[pos])++pos;
			if(pos!=len) aa.push_back(str[pos]);
			++pos;
		}
		ans = 0;
		if(aa.size()==1  && aa[0]=='+') ans = 0;
		else if(aa.size()==1 && aa[0]=='-') ans = 1;
		else if(aa[0]=='+'){
			ans = aa.size()/2;
			ans = ans*2;
		}
		else if(aa[0]=='-'){
			if(aa.size()%2==0) ans = aa.size()-1;
			else ans = aa.size();
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
