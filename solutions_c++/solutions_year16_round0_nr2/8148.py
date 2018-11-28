#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		string s;
		cin>>s;
		
		int j;
		for(j=s.length()-1;j>=0;j--){
			if(s[j]=='-')break;
		}
		if(j==-1){
			cout<<"Case #"<<i<<": "<<0<<endl;
		}
		else{
			int count=0;
			for(int k=1;k<=j;k++){
				if(s[k]!=s[k-1])count++;
			}
			cout<<"Case #"<<i<<": "<<count+1<<endl;
		}
		
		
	}
	return 0;
}