#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int MAXN = 200;

void reverse(char dat[MAXN], int n){
	for(int i=0;i<n/2;i++){
		char tmp = dat[n-1-i];
		dat[n-1-i] = dat[i];
		dat[i] = tmp;

		dat[i] = '+' + '-' - dat[i];
		dat[n-1-i] = '+' + '-' - dat[n-1-i];
	}

	if(n%2==1){
		dat[n/2] = '+' + '-' - dat[n/2];
	}
}

int solve(char dat[MAXN], int size){
	if(size==0) return 0;	
	int cnt = 1;
	while(cnt<size&&dat[cnt] == dat[cnt-1]){
		cnt++;
	}
	if(cnt == size){
		if(dat[0]=='+') return 0;
		return 1;
	}

	reverse(dat, cnt);
	return solve(dat,size)+1;
}

int main()
{
	char dat[MAXN];
	int size;
	int T;
	cin >> T;
	for(int i = 1;i<=T;i++){
		scanf("%s",dat);
		printf("Case #%d: ",i);
		int ans = solve(dat, strlen(dat));
		printf("%d\n",ans);
	}
	return 0;
}
