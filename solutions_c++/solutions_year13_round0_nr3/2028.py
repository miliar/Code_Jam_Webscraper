#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

#define N 100000000000004
#define ulli unsigned long long int

vector<ulli> num;

int f(ulli n){
	int v[20], i = 0, k, j;
	while(n){
		v[i++] = n%10;
		n/=10;
	}
	for(j = 0, k = i-1; j < k; ++j, --k)
		if(v[j] != v[k]) return 0;
	return 1;
}

int main(){
	ulli a, b, i;
	int t;
	
	scanf("%d", &t);
	for(i = 1; i < sqrt(N)+10; ++i){
		if(f(i) && f(i*i) && i*i < N)
			num.push_back(i*i);
	}
	
	for(int k = 0; k < t; ++k){
		scanf("%llu %llu", &a, &b);
		vector<ulli>::iterator l, r;
		int aux;
		l = lower_bound(num.begin(), num.end(), a);
		r = lower_bound(num.begin(), num.end(), b);
		if(*l == a && *r == b) aux = 1;
		else if(*l != a && *r == b) aux = 1;
		else if(*l == a && *r != b) aux = 0;
		else if(*l != a && *r != b) aux = 0;
		printf("Case #%d: %llu\n", k+1, (ulli)((r-l)+aux));	
	}

return 0;
}
