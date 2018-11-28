//============================================================================
// Name        : jam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {


#ifndef ONLINE_JUDGE
 freopen("D:\\A-large.in","rt",stdin);
 freopen("D:\\out.out","wt",stdout);
#endif


	int test;
	cin>>test;
	for (int l=1;l<=test;l++){
	int max;
	string values;
	map <int,int> mp;
	cin>>max>>values;
	for (int i=0;i<=max;++i){
		mp[i]=values[i]-'0';
	}
int cnt=0,all=0,temp=0;
for (int j=0;j<=max;j++){
	if(all>=j){
		all+=mp[j];
	}
	else{
		cnt=j-(all+temp);
		if(cnt>0)
		temp+=cnt;
		all+=mp[j];
	}
}
cout<<"Case"<<" #"<<l<<": "<<temp<<endl;
	}
	return 0;
}
