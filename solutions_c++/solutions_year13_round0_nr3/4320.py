
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

vector<long long> fair;

long long isPerfectSquare(long long a){
	long long b = sqrt(a);
	return (b * b) == a ? b : -1ll;
}

bool isPalindrome(long long n){
	long long tmp = n;
	long long m = 0;
	while(tmp){
		m = m * 10 + (tmp % 10);
		tmp /= 10;
	}
	return m == n;
}

void pre(){
	for(long long i = 1; i <= 10000000; i++){
		if(isPalindrome(i) && isPalindrome(i * i)){
			fair.push_back(i * i);
		}
	}
}
int main() {
	freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	pre();
	long long t, a, b;
	cin >> t;
	for(int c = 1; c <= t; c++){
		cin >> a >> b;
		int cnt = 0;
		for(int i = 0; i < fair.size(); i++){
			if(fair[i] >= a && fair[i] <= b){
				cnt++;
			}
		}
		printf("Case #%d: %d\n", c, cnt);
	}
	return 0;
}

