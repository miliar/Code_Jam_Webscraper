#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
using namespace std;
int main() {
	int t;
	scanf("%d",&t);
	string str;
	for(int i=1;i<=t;i++) {
		cin>>str;
		string res="";
		char head = str[0];
		res+=head;
		for(int j=1;j<str.length();j++) {
			if(str[j]>=head) {
				res=str[j]+res;
				head=str[j];
			}
			else {
				res+=str[j];
			}
		}
		cout<<"CASE #"<<i<<": "<<res<<endl;
		
	}
}
