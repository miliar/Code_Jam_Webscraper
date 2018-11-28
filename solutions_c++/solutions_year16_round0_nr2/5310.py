#include <iostream>
#include <cstdio>
using namespace std;

int solve(){
	string str;
	char t;
	cin >> str;
	int cou=0,i,ri,l=str.length();
	bool chk;
	while(1){
		chk=false;
		ri=0;
		i=0;
		while(str[i]=='+'&&i!=l){
			str[i]='-';
			chk=true;
			++i;
		}
		if(i==l)
			chk=false;
		else if(i==0){
			for(i=l-1;i>=ri;--i){
				if(str[i]=='-')
					chk=true;
				if(chk){
					if(str[i]=='-')
						t='+';
					else if(str[i]=='+')
						t='-';
					if(str[ri]=='-')
						str[i]='+';
					else if(str[ri]=='+')
						str[i]='-';
					str[ri]=t;
					++ri;
				}
			}
		}
		if(chk==false)
			return cou;
		++cou;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i)
		printf("Case #%d: %d\n",i,solve());
}