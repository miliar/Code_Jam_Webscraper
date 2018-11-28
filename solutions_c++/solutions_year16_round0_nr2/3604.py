#include<bits/stdc++.h>
using namespace std;
int main(){
unsigned long long int t,i,j,l,c=0;char s[105];cin>>t;
	for(j=1;j<=t;j++){
		c=0;
	cin>>s;
		l = strlen(s);
		while(1){
			i=0;
			if(s[i]=='+'){
				while(s[i]=='+' && i<l){
					i++;
				}
				if(i==l){
					break;
				}
				else{
					memset(s,'-',sizeof(char)*(i+1));
					c+=1;
				}
			}
			else if(s[i]=='-'){
				while(s[i]=='-' && i<l){
					i++;
				}
				if(i==l){
					c+=1;
					break;
				}
				else{
					memset(s,'+',sizeof(char)*(i+1));
					c+=1;
				}
 
			}
		}
		cout<<"case #"<<j<<": "<<c<<"\n";
	}
	return 0;
}
