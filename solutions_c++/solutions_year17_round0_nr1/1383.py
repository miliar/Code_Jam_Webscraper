#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
	int T;	cin>>T;
	for(int t=1;t<=T;t++){
		string s;	int k;	cin>>s>>k;
		int ret=0;
		for(int i=k-1;i<s.size();i++){
			if(s[i-k+1]=='-'){
				ret++;
				for(int j=i-k+1;j<=i;j++){
					if(s[j]=='+')	s[j]='-';
					else 	s[j]='+';
				}
			}
		}
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				ret=-1;
				break;
			}
		}
		cout<<"Case #"<<t<<": ";
		if(ret==-1)	cout<<"IMPOSSIBLE"<<endl;
		else 	cout<<ret<<endl;
	}
	return 0;
}