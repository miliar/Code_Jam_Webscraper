/*
 * ProbC.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: nataraj
 */




#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <iterator>
#include <sstream>
#include <algorithm>
using namespace std;

int T,prob;
int r,t;
vector<int> res;

void init(){
	int sum=0;int i=2;
	while(sum<1000){
		sum+=(2*i-1);
		res.push_back(sum);
		i+=2;
	}
}

void solve(){
	long long ans=0;
	long long sum=0;

	long long temp=r+1;
	while(sum<=t){
		sum+=((temp<<1)-1);
		++ans;
		temp+=2;
	}
	printf("Case #%d: %lld\n", prob++, ans-1);
}
int main(int argc, char **argv) {
//	init();
	scanf("%d",&T);prob=1;
//	long long xx = 100000000000000;
//	printf("%lld\n",xx);
	while(T--){
		scanf("%d%d",&r,&t);
		solve();
//		printf("Case #%d: %s\n", prob++, solve());
	}
//	while(1){
//	string s;cin>>s;
//	cout<<getNextPalin(s);
//	}
	return 0;
}
