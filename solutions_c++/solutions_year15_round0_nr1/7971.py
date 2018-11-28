//============================================================================
// Name        : CodejamQualification.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("/home/al/workspace3/CodejamQualification/in.txt","r",stdin);
	int t,smax,s[1001];
	string str;
	cin>>t;
	for(int k=0;k<t;k++){
		cin>>smax;
		cin>>str;

		for(int i=0;i<=smax;i++){
			s[i] = str[i]-48;
		}//not needed ....

		int uthe=s[0],needed,ans=0,
		max = 0;
		for(int i=1;i<=smax;i++){
			needed = i-uthe;
			needed = needed>0?needed:0;
			uthe = uthe+s[i];
			max = needed>max?needed:max;
		}
		cout<<"Case #"<<k+1<<": "<<max<<endl;
	}
	return 0;
}
