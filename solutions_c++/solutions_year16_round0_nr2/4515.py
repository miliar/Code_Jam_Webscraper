#include<iostream>
#include<unistd.h>
using namespace std;
int done(string s){

	int i=0;
	while(i<s.length()){
		if(s[i]=='-')
			return 0;
		i=i+1;
	}
	return 1;

}
int main(){


	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++){
		int res=0;
		cout<<"CASE #"<<i<<": ";
		string s;
		cin>>s;
		//cout<<s.length()<<endl;
		if(s.length()==0){
		
			cout<<"0"<<endl;
		}
		else{
		
			while(done(s)!=1){
			
				if(s[0]=='-'){
					int j=1;
					while(j<s.length()&&s[j]!='+'){
						j++;
					}
					for(int k=0;k<j;k++){
					
						s[k]='+';
					
					}
				}
				else{
					int j=1;
					while(j<s.length()&&s[j]!='-'){
						j++;
					}
					for(int k=0;k<j;k++){
					
						s[k]='-';
					
					}
					
				
				}
				res++;
			}
		
			cout<<res<<endl;
		}
	
	}


}
