#include <iostream>
#include<bits/stdc++.h>
#define forn(i,n) for(i=0;i<n;i++)
using namespace std;
typedef long long int lli;

int main() {
	// your code goes here
	int counter=0;
	lli t;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		lli i=0;
		lli l=s.size();
		
		int j=0;
		for(i=1;i<l;i++){
			if(s[i]>=s[0]){
				char pop=s[i];
				for(j=i;j>0;j--){
					s[j]=s[j-1];
				}
				s[0]=pop;
			}
		}

	cout<<"Case #"<<++counter<<": ";
	for(i=0;i<=l;i++){

			 cout<<s[i];
		
	}
	cout<<endl;
	}
	
	
	
	
	
	
	
	
	return 0;
}