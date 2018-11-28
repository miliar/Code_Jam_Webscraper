#include <stdio.h>
#include <iostream>
#include <set>
using namespace std;


void  check(set<int> & s, int n){
	if(n==0) {
		s.insert(0);
		return;
	}
	
	while(n){
		s.insert(n % 10);
		n = n / 10;	
	}
}

int solve(long long  n){
	long long last_sum = -1;
	long long sum = n;
	set<int> s;
	int cnt = 0;
	while(last_sum != sum && s.size()!=10){
		check(s, sum);
		last_sum = sum;
		sum = sum + n;
		cnt ++;
	}
	if(s.size()==10) return last_sum;
	return -1;
}

int main()
{
	int T;
	long long n;
	cin >> T;
	for(int i = 1;i<=T;i++){
		cin >> n;
		printf("Case #%d: ", i);
		int ans = solve(n);
		if(ans>=0)
			printf("%d\n", ans);
		else
			printf("INSOMNIA\n");
	}
	return 0;
}

