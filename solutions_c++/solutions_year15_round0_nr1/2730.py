#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int T,N;
string s;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t ++){
		scanf("%d", &N);
		cin >> s;
		int org = 0;
		int sum = 0;
		for(int i = 0 ; i < s.length() ; i ++){
			int d = s[i]-'0';
			org += d;
			if(sum < i) sum += i-sum+d;
			else sum += d;
		}
		printf("Case #%d: %d\n", t, sum-org);
	}
	return 0;
}
