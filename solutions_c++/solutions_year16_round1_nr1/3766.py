#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		string s;cin>>s;
		vector<char> v1;
		vector<char> v2;
		char msc;
		v1.push_back(s[0]);
		msc=s[0];
		for(int i=1;i<s.length();i++){
			if(s[i]>=msc){
				v1.push_back(s[i]);
				msc=s[i];
			}
			else 
				v2.push_back(s[i]);
		}
		cout<<"Case #"<<t<<": ";
		for(int i=v1.size()-1;i>=0;i--)
			printf("%c",v1[i]);
		for(int i=0;i<v2.size();i++)
			printf("%c",v2[i]);
		printf("\n");
	}
}