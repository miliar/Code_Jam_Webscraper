#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	string s;
	for(int i=0;i<t;i++){
		cin>>s;
		long l=0;
		for(long j=s.size()-1;j>=0;j--){
			if(s[j]=='+'){if(l%2!=0)l=l+1;}
			else{if(l%2==0)l=l+1;
			}
				
		}
		cout<<"Case #"<<i+1<<": "<<l<<endl;
	}
}
