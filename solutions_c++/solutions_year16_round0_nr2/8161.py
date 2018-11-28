#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int t,len;
	char str[101];
	cin>>t;
	for(int k=1; k<=t; k++){
		int cnt=0;
		cin>>str;
		len=strlen(str);
		cout<<"Case #"<<k<<": ";
		if(str[len-1]=='-')
			cnt++;
		if(len==1){			
			cout<<cnt<<endl;
			continue;
		}
		for(int i=1; i<len;i++){
			if(str[i]!=str[i-1])
				cnt++;
		}
		cout<<cnt<<endl;
	}
}