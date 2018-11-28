#include<iostream>
#include<string>
using namespace std;
main(){
	int t,j;
	cin>>t;
	for(j=1;j<=t;j++){
		int flag,count=0;
		string s,plus,minus,tmp_plus,tmp_minus;
		//cin.getline(s);
		cin>>s;
		for(int k=0;k<s.length();k++){
			plus+="+";
			minus+="-";
		}
		int size=s.length();
		while(1){
		
		if(s[0]=='+')
				flag=1;
		else
				flag=2;		
		
			if(flag==1){
				for(int i=0;i<size;i++){
					if(s[i]=='-'){
						tmp_minus=minus.substr(0,i);
						s.replace(0,i,tmp_minus);
						count++;
						flag=3;
						break;
					}
					
				}//end of for
				if(flag==1){
					//cout<<"Case #"<<j<<": "<<count<<endl;
					//count=0;
					flag=5;
				}
				else{
					flag=1;
				}
				
			}//end of if
			
			else	if(flag==2){
				for(int i=0;i<size;i++){
					if(s[i]=='+'){
						tmp_plus=plus.substr(0,i);
						s.replace(0,i,tmp_plus);
						count++;
						flag=4;
						break;
					}
					
				}//end of for
				if(flag==2){
					s=plus;
					count++;
				}
				else{
					flag=2;
				}
				
			}//end of else
			
			if(flag==5){
				break;
			}
					
	}//end of while
		if(flag==5){
					cout<<"Case #"<<j<<": "<<count<<endl;
					count=0;
					flag=1;
				}
		
	}//end of test cases
	
	
}



