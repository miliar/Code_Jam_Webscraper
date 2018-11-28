#include <iostream>
using namespace std;

int main() {
	int t,k=1;
	cin>>t;
	while(k<=t){
		int m;
		string s;
		cin>>m>>s;
		int a[m+1];
		for(int i=0;i<=m;i++){
			a[i]=s[i]-48;
		}
		int j=0,sum=0,ct=0;
		while(j<m){
			sum=sum+a[j];
			if(j+1>sum){
				ct=ct+j+1-sum;
				sum=j+1;
			}
			j++;
		}
		cout<<"Case #"<<k<<": "<<ct<<endl;
			
		k++;
		}
	
	
	
	// your code goes here
	return 0;
}