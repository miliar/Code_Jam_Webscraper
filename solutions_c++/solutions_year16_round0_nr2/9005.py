#include <iostream>
using namespace std;
string reverse(string s1){
	string s2="";
	for(int i=s1.length()-1;i>=0;i--){
		if(s1.at(i)=='+')
			s2+="-";
			else s2+="+";
	}
	return s2;
}
int func(string s){
	int res=0;
	int p=0;//0 => pos
	while(1){
	int length= s.length();
	if(length==0)
		return res;
	int i=length;
	if(p==0){
	for(i=length-1;i>=0;i--)
		if(s.at(i)=='-')
			break;
	}else{
		for(i=length-1;i>=0;i--)
		if(s.at(i)=='+')
			break;
	}
	if(i<0)
		return res;
	string s1 = s.substr(0,i+1);
	// res++;
	// s1=reverse(s1);
	if((s1.at(0)=='-'&&p==0)||(s1.at(0)=='+'&&p==1)){
		res+=1;
		//simply reverse
		string s2= reverse(s1);
		s=s2;
	}
	else if(s1.at(0)=='+'){
		p=1;
		res+=1;
		s=s1;
		
	}
	else {
		p=0;
		res+=1;
		s=s1;
	}
	
	
		
	}		
	
}

int main() {
	// your code goes here
	int t;
	string s;
	cin>>t;
	for(int w=1;w<=t;w++){
		cin>>s;

			cout<<"Case #"<<w<<": "<<func(s)<<endl;
		
			
	}
	return 0;
}

