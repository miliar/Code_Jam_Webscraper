#include<iostream>
using namespace std;

int count_flips(string s){
int count=0;
for(int i=0;i<s.length();){
	if(s[i]=='+'){
		int temp=i;
		while(i<s.length() && s[i]!='-'){
			i++;
		}
		if(i==s.length()){
			return count;
		}
		else{
			count++;
				
		}
	}
	if(s[i]=='-'){
		count++;
		while(i<s.length() && s[i]!='+' ){
			i++;		
		}
		if(i==s.length()){
			return count;		
		}

	}



}
return count;

}



int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string s;
		cin>>s;
		cout<<"Case #"<<i+1<<": "<<count_flips(s)<<endl;
}
}
