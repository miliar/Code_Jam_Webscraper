#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <stack>

using namespace std;

int N, J;
int a[50];
int num;
int prime[100000];
int len_prime = 0;
int p[1000000];
void make_prime(){
	memset(p, 0, sizeof(p));
	for (int i = 2; i <= 1000000; i++)
		if (!p[i]){
			prime[len_prime++] = i;
			int j = i+i;
			while (j<=1000000){
				p[j] = 1;
				j = j + i;
			}
		}
}

unsigned long long proof[10];

unsigned long long get_num(int b){
	unsigned long long sum = 1;
	unsigned long long t = 1;

	for (int i = 1; i < N; i++){
		t *= b;
		if (a[i])
			sum += t;
	}

	return sum;
}

unsigned long long get_proof(unsigned long long x){
	for (int i = 0; i < len_prime; i++){
		if (prime[i] >= x)
			return 1;
		if (x % prime[i] == 0)
		 	return prime[i];
	}
	return 1;
}

void check(){
	int ok = 1;
	for (int b = 2; b <= 10; b++){
		unsigned long long x = get_num(b);
		proof[b] = get_proof(x);
		if (proof[b] == 1){
			ok = 0;
			break;
		}	
	}

	if (ok){
		for (int i = N-1; i >=0; i--)
			cout << a[i];
		for (int i = 2; i <= 10; i++)
			cout << " " << proof[i];
		cout << endl;

		num ++;
	}
}

void solve(int i){
	if (i == N-1){
		check();
		return ;
	}

	for (int j = 0; j <= 1; j++){
		a[i] = j;
		solve(i+1);
		if (num == J)
			return;
	}
}

int main() {

	make_prime();
	
	int T;
	cin >> T;
	cin >> N >> J;
	memset(a, 0, sizeof(a));
	a[0] = 1;  
	a[N-1] = 1;

	num = 0;
	cout << "Case #1:" << endl;
	solve(1);
	return 0;
}



