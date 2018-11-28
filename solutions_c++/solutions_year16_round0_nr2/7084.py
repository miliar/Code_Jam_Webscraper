#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int m,cnt=0;
	cin>>m;
	while(m--){
		cnt++;
		char s[100];
		cin>>s;
		int n=strlen(s);
		int c=0,c1=0;
		for(int i=0;i<n;i++){
			if(s[i]=='+'){
				c++;
			}
			else{
				c1++;
			}
		}
		if(c==n){
			cout<<"Case #"<<cnt<<": "<<0<<endl;
		}
		else if(c1==n){
			cout<<"Case #"<<cnt<<": "<<1<<endl;
		}
		else{
			int c2=0;
			for(int i=0;i<n-1;i++){
				if(s[i]==s[i+1]){
					continue;
				}
				else{
					c2++;
					for(int j=0;j<i;j++){
						s[j]=s[i];
					}
				}
			}
			if(s[0]=='-'){
				cout<<"Case #"<<cnt<<": "<<c2<<endl;
			}	
			else{
				cout<<"Case #"<<cnt<<": "<<c2+1<<endl;
			}
		}
	}
}