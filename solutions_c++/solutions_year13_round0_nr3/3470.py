#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int palindromes(int x){
	if(x < 0) return 0;
	int y = 0, z = x;
	while(z != 0){
		y = y * 10 + z % 10;
		z /= 10;
	}
	if(x == y) return 1;
	else return 0;
}

int slution(int a, int b){
	int ans = 0;
	for(;; ++a){
		int x = a * a;
		if(x > b) break;
		if(palindromes(a) && palindromes(x))
			++ans;
	}
	return ans;
}

int main(void){
	int n, i = 0, a, b;
	cin >> n;
	while(i++ < n){
		cin >> a >> b;
		int x = sqrt(a);
		if(x * x < a) x += 1;
		printf("Case #%d: %d\n", i, slution(x, b));
	}
	return 0;
}