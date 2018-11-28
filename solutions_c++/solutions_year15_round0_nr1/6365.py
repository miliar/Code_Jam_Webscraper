//============================================================================
// Name        : justcon.cpp
// Author      : sara.cpp
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
#define mp make_pair
#define ll long long
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	int t,x;
	string s;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		long long sum=0;
		int count=0;
		scanf("%d",&x);
		cin>>s;
		sum+=s[0]-'0';
		for(int j=1;j<s.size();++j){
			if(s[j]=='0')
				continue;
			if(sum>=j)
				sum+=s[j]-'0';
			else{
				count+=(j-sum);
				sum+=(j-sum);
				sum+=s[j]-'0';
			}
		}
		printf("Case #%d: ",i);
		printf("%d\n",count);
	}
	return 0;
}
