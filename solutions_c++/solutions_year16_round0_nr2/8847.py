#include<bits/stdc++.h>
using namespace std;

bool checkstr(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='-') return false;
	}
	return true;
}

int posminus(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='-') return i;
	}
	return -1;
}

int posplus(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='+') return i;
	}
	return -1;
}

int main(){
	int T,val=1;
	cin>>T;
	while(T--){
		string s;
		cin>>s;
		int cnt=0;
	q:	if(checkstr(s)){
			printf("Case #%d: %d\n",val,cnt);
		}
		else{
			
	si:		int k= posminus(s),i;
			if(k!=-1 && k!=0) cnt++;
			for(i=0;i<k && k!=-1;i++){
				s[i] = '-';
			}
			if(checkstr(s)) goto q;
			k = posplus(s);
			if(k!=-1) cnt++;
			else if(k==-1){
				cnt++;
				for(int i=0;i<s.length();i++) s[i]='+';
				goto q;
			}
			for(int i=0;i<k && k!=-1;i++){
				s[i] = '+';
			}
			if(checkstr(s)) goto q;
			else goto si;
		}
		val++;
	}
	return 0;
}

