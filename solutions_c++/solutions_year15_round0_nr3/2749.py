#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

int main(){
	int t;
	int l,x;
	string s;
	vector<char> v;
	int neg;
	char ch;
	short cond;
	
	cin>>t;
	for(int k=1 ; k<=t ; k++){
		scanf("%i%i",&l,&x);
		cin>>s;
		v.resize(l*x);
		for(int i=0 ; i< l*x ; i++){
			v[i]=s[i%l];
		}
		
		neg=0;
		ch = v[0];
		cond=0;
		for(int i=1 ; i<=v.size() ; i++){
			if(ch=='i' && cond==0){
				cond++;
					ch=v[i];
				continue;
			}
			else if(ch=='j' && cond==1){
				cond++;
					ch=v[i];
				continue;
			}
			else if(i==v.size() && cond==2){
				if(ch=='k'){
					cond++;
					break;
				}
			}		
			if(i==v.size()){
				break;
			}
			
			if(ch=='1'){
				ch=v[i];
			}
			
			else if(ch=='i'){
			
				if(v[i]=='i'){
					ch='1';
					neg++;
					neg=neg%2;
				}
				else if(v[i]=='j'){
					ch='k';
				}
				else{
					ch='j';
					neg++;
					neg=neg%2;
				}
			}
			else if(ch=='j'){
				if(v[i]=='i'){
					ch='k';
					neg++;
					neg=neg%2;
				}
				else if(v[i]=='j'){
					ch='1';
					neg++;
					neg=neg%2;
				}
				else{
					ch='i';
				}
			}
			else{
				if(v[i]=='i'){
					ch='j';
				}
				else if(v[i]=='j'){
					ch='i';
					neg++;
					neg=neg%2;
				}
				else{
					ch='1';
					neg++;
					neg=neg%2;
				}
			}
		}
		if(cond==3 && neg==0){
			printf("Case #%i: YES\n",k);
		}
		else{
			printf("Case #%i: NO\n",k);
		}
	}
}
