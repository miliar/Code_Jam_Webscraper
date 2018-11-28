//============================================================================
// Name        : CPP.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<iostream>
using namespace std;
#define maxn 10000000
bool check(long long n){
	char str[20];
	sprintf(str,"%lld",n);
	int len = strlen(str);
	for(int i=0;i<len;i++){
		if(str[i] != str[len - i -1])return false;
	}
	return true;
}
long long result[55];
int main(){
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	int cases,cas;
	cin >> cases;
	long long A,B;
	int cnt=0;

	for(long long i = 1;i<= maxn;i++){
		if(check(i) && check(i*i)){
			result[cnt++] = i * i;
		}
	}
	for(int cas = 1;cas <= cases; cas++){
		cin >> A >> B;
		int ans = 0;
		for(int i = 0;i < cnt;i++ ){
			if(result[i] >= A && result[i] <= B){
				ans++;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
