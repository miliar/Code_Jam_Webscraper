#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>

using namespace std;


char str[110];
int N;

int count(){
	int ct =0,i;

	for(i = 0; i < N; ++i){
		if(str[i] == '+') continue;
		if(i && str[i] == str[i-1]) continue;
		ct += 2;
	}

	if(str[0] == '-') --ct;
	return ct;
}

int main(){

	int t,x;
	scanf("%d",&t);

	for(x =1;x<= t; ++x){
		scanf("%s",str);
		N = strlen(str);
		printf("Case #%d: %d\n",x,count());
	}


	return 0;
}
