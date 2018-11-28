#include<cstdio>
#include<iostream>

using namespace std;

int A[1010];
int round, md, total, div;

void red() {
	total -= A[1];
	for(int i=1; i<md; i++) {
		A[i] = A[i+1];
	}
	A[md] = 0;
	md--;
}

void half() {
	int a = md / 2;
	int b = md - a;
	A[a]++; A[b]++; A[md]--; total++;
	while(A[md]==0) md--;
}

int eat() {
	
	md = 0;
	
	for(int i=1; i<=1000; i++) {
		total += A[i];
		if (A[i] > 0) {
			md = i;
		}
	}
	
	int res = md;
	int thres = md - 1;
	
	while(thres > 0) {
		div = 0;
		for(int i=thres + 1; i<=md; i++) {
			div += A[i] * ((i - 1) / thres);	
		}	
		
		res = min(res, thres + div);
		thres--;
	}
	
	return res;		
}

int main() {
	
	freopen("F:\\Dev C++\\B-large.in", "r", stdin);
	freopen("F:\\Dev C++\\B-large.out", "w", stdout);
	
	int tc, x, n;
	scanf("%d", &tc);
	
	for(int k=1; k<=tc; k++) {
		for(int i=0; i<=1000; i++) A[i] = 0;
		
		scanf("%d", &n);
		
		A[0] = 1;
		
		for(int i=1; i<=n; i++) {
			scanf("%d", &x);
			A[x]++;
		}
		
		int res = eat();
		printf("Case #%d: %d\n", k, res);	
	}
}
