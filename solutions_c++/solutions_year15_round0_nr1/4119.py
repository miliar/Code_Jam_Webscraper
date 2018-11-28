//============================================================================
// Name        : Contest.cpp
// Author      : Alireza
// Version     :
// Copyright   : Enjoy It!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstring>

#define FOR(i,c,n) for(int i=(c);(i)<(n);++(i))
#define FR(i,n) FOR(i,0,n)
using namespace std;


int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tcase;cin>>tcase;
	FR(cas,tcase){
		printf("Case #%d: ",cas+1);
		int n;string s;
		cin>>n>>s;
		int sum=0,res=0;
		FR(i,s.size()){
			if(i>sum) res=max(res,i-sum);
			sum+=s[i]-'0';
		}
		cout<<res<<endl;
	}
}
