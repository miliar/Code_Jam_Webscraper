#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t,i,j,k,l,count,flag;
	cin>>t;
	for(k=1;k<=t;++k){
		char x[1000],s[1000];
	
		cin>>x;
		count=0;
		l=0;
		flag=0; // +
		for(i=0;x[i]!='\0';++i){
			if(i==0){
				s[l++]=x[i];
			}else if(s[l-1]!=x[i]){
				s[l++]=x[i];
			}
		}
		s[l]='\0';
		//cout<<s<<"\n";
		cout<<"Case #"<<k<<": ";
		
		if(s[0]=='+'){
			if(l%2==0)cout<<l<<"\n";
			else cout<<((l-1)/2)*2<<"\n";
		}else {
			if(l%2==0) cout<<1+2*((l-2)/2)<<"\n";
			else cout<<1+2*((l-1)/2)<<"\n";
		}
	
		
		/*if(flag==1) cout<<x*i;
		else cout<<"INSOMNIA";
		cout<<"\n";*/
	}
	
	return 0;
}
