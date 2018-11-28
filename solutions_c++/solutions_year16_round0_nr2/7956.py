#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
long long int t,i,j,len,c=0;char s[100001];
	cin>>t;
	for(int v=1;v<=t;v++){
		c=0;
	cin>>s;
		len = strlen(s);
		while(1){
			i=0;
			if(s[i]=='+'){
				while(s[i]=='+' && i<len){
					i++;
				}
				if(i==len){
					break;
				}
				else{
					//memset(s,'-',sizeof(char)*(i+1));
					for(int h=0;h<i+1;h++)
						s[h]='-';
		
					c+=1;
				}
			}
			else if(s[i]=='-'){
				while(s[i]=='-' && i<len){
					i++;
				}
				if(i==len){
					c+=1;
					break;
				}
				else{
						for(int h=0;h<i+1;h++)
						s[h]='+';
				
					c+=1;
				}
 
			}
		}
		cout<<"Case #"<<v<<": "<<c<<"\n";
	}
	return 0;
}
