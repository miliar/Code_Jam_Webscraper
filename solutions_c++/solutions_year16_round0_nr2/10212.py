#include <iostream>
#include<string>
using namespace std;

int main() {
	long long int t,cas=1,i,len;
	string str;
	
	cin>>t;
	while(t--){
		cin>>str;
		len=str.length();
		int minways[len+1]={0};
		if(len==1) {cout<<"Case #"<<cas++<<": "<<(str[len-1]=='-'?minways[len-1]+1:minways[len-1])<<endl;
		continue;}
		if (str[0]==str[1])
			minways[0]=0;
		else
			minways[0]=1;	
			
		for (i=1; i<len;++i){
			if(str[i]==str[i+1])
				minways[i]=minways[i-1];
			else
				minways[i]=minways[i-1]+1;
		}
		//cout<<str;
		cout<<"Case #"<<cas++<<": "<<(str[len-1]=='-'?minways[len-1]+1:minways[len-1])-1<<endl;
		
	}
	return 0;
}