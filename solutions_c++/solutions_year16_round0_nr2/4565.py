#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,t,i,l,xx=1,f,pos1,pos2;
	string s;
	cin>>t;
	while(t--){
		cin>>s;
		cout<<"Case #"<<xx++<<": ";
		l=s.length();
		int cnt=0;
		while(1){
			i=0;
			f=0;
			pos1=-1;
			pos2=-1;
			for(i=0;i<l;i++){
				if(s[i]=='+'){
					pos1=i;
				}
				else
					break;
			}
			if(i==l)
				break;
			for(i=0;i<=pos1;i++){
				s[i]='-';
			}
			if(pos1!=-1)
				cnt++;
			for(i=0;i<l;i++){
				if(s[i]=='-'){
					s[i]='+';
				}
				else
					break;
			}
			cnt++;
		}
		cout<<cnt<<endl;
	}
}
