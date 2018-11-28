#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, n) FOR(i, 0, n)
using namespace std;

string to_string(int num) {
	string res;
	while(num) {
		res += (num%10)+'0';
		num /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}

int qtd[1005];
bool is_ok[1005];
bool palindrome(int num) {
	string res = to_string(num);
	int tam = res.size();
	FORR(i, tam/2) {
		if(res[i] != res[tam-i-1]) return false;
	}
	return true;
}

void calc() {
	memset(qtd, 0, sizeof(qtd));
	memset(is_ok, false, sizeof(is_ok));
	for(int i = 1; i*i <= 1000; i++) {
		if(palindrome(i) && palindrome(i*i)) is_ok[i*i] = true;
	}
	for(int i = 1; i <= 1000; i++)
		qtd[i] = qtd[i-1]+is_ok[i];
}

int main() {
	int t, a, b;
	calc();
	scanf("%d", &t);
	FORR(i, t) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i+1, qtd[b]-qtd[a-1]);
	}
}
