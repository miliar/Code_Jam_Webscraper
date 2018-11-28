#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
int main(){
	int N;

	scanf("%d",&N);

	for(int iii=1;iii<=N;iii++){
		int n;string st;
		cin>>st;
		bool f;
		int c=0;int s=0;
		for(int i=0;i<(int)st.size();i++){
			if(s>=i)s+=(st[i]-'0');
			if(i>s&&st[i]-'0'>0){c+=i-s;s=i+(st[i]-'0');}
		}
		cout<<"Case #"<<iii<<": "<<c<<endl;
	}
	return 0;
}
