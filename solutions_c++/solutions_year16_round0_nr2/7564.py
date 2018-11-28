#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ci=1;ci<=t;++ci){
		string s,q="";
		cin>>s;
		q+=s[0];
		int sl=s.size();
		for(int i=1;i<sl;++i){
			if(s[i-1]!=s[i]){
				q+=s[i];
			}
		}
		int k=q.size();
		if(q[k-1]=='+'){
			--k;
		}
		printf("Case #%d: %d\n",ci,k);
	}
	return 0;
}
