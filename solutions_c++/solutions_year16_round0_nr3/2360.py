#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <iostream>

using namespace std;

long long check(int t[16], int b){
	long long base = 1;
	long long n = 0;
 	for(int i = 0;i<16;i++){
		n = n + t[i] * base;
		base = base * b;
	}
	for(int i = 2;i<1000 && i < n;i++){
		if(n % i == 0) return i;
	}
	return -1;
}

bool check(int t[16]){
	long long div[10];
	bool flag = true;
	for(int i=2;i<=10;i++){
		div[i] = check(t,i);
		if(div[i] < 0){
			flag = false;
			break;
		}
	}
	if(flag){
		for(int i=15;i>=0;i--) printf("%d",t[i]);
		for(int i = 2; i<=10;i++) cout << " " <<  div[i];
		printf("\n");
	}
	return flag;
}

void solve(){
	int t[16];
	t[0] = 1;
	t[15] = 1;
	set<int> s;
	while(s.size()<50){
		for(int i = 1; i < 15; i++){
			t[i] = rand()%2;	
		}
		int n = 0;
		int b = 1;
		for(int i = 0;i<16;i++){
			n += t[i] * b;
			b = b * 2;
		}

		if(s.count(n)==0){
			if(check(t)){
				s.insert(n);
			}
		}
	}
}

int main()
{
	printf("Case #1:\n");
	solve();
	return 0;
}
