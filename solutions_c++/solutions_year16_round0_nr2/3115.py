#include<bits/stdc++.h>
using namespace std;
void reverse(string &s,int i, int j) {
	while(i<j){
		char t = s[i];
		s[i]=s[j];
		s[j]=t;
		if(s[i]=='-') s[i]='+';
		else s[i]='-';
		if(s[j]=='-') s[j]='+';
		else s[j]='-';
		i++;
		j--;
	}
	if(i==j){
		if(s[i]=='-') s[i]='+';
		else s[i]='-';
	}
}
int done(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]=='-') return 0;
	}
	return 1;
}
int main() {
	ifstream oo;
	oo.open("B-large.in");
	ofstream mm;
	mm.open("op4.txt");
	
	int t,i,k;
	oo>>t;
	for(i=1;i<=t;i++){
		string s;
		oo>>s;
		int flag=0;
		long int c=0;
		if(s.length()==1){
			if(s[0]=='-') c=1;
			mm<<"Case #"<<i<<": "<<c<<endl;
			continue;
		}
		while(flag==0){
			/*if(done(s)){
				flag=1;
				break;
			}*/
			if(s[0]=='-'){
				k=s.length()-1;
				while(s[k]=='+'){
					k--;
				}
				reverse(s,0,k);
				c++;
			} else {
				k=s.length()-1;
				while(s[k]=='+' && k>=0) k--;
				if(k<0) {
					flag=1;
					break;
				}
				while(s[k]=='-') k--;
				reverse(s,0,k);
				c++;
			}
			
		}
		mm<<"Case #"<<i<<": "<<c<<endl;
	}
	return 0;
}
