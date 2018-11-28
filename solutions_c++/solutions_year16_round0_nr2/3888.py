#include<bits/stdc++.h>
using namespace std;

int main() {
	long long testes;
	scanf("%lld",&testes);
	int casos=1;
	while(testes-->0) {
		string S;
		cin >> S;
		long long total=1;
		for(int i=1; i<S.size(); i++){
			total+=(S[i]!=S[i-1]);
		}
		total-=(S[S.size()-1]=='+');
		printf("Case #%d:", casos++);
		printf(" %lld\n", total);
	}
	return 0;
}