#include <bits/stdc++.h>
using namespace std;
inline int pos(string s){
	for(int i=s.size()-1;i>=0;i--)if(s[i]=='-')return i+1;
	return 0;
}
inline void f(string &s){
	int end=pos(s);
	for(int i=0;i<end;i++){
		s[i]=(s[i]=='-')?'+':'-';
	}
}
int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string s;
		cin>>s;
		int operations = 0;
		while(pos(s)!=0){
			f(s);
			operations++;
		}
		printf("Case #%d: %d\n",i+1,operations);
	}
	return 0;
}


