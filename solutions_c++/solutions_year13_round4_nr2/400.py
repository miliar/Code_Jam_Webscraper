#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<utility>
#include<iostream>
#include<sstream>
#include<fstream>

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);
const int maxn = 600000;

int ntest;
int answer;

int N;
long long P;
long long X, Y;

long long worst(long long X) {
	long long front = X;
	long long lead = 0;
	long long total = (1ll<<N);

	while(front > 0) {
		lead += total / 2;
		front = (front - 1) / 2;
		total /= 2;
	}

	return lead + 1;
}

long long best(long long X) {
	long long L = X;
	long long R = (1ll<<N) - L - 1;
	long long lead = 0;
	long long total = (1ll<<N);

	while(R) {
		R--;
		if(L%2) {
			R--;
			L = (L+1)/2;
			R /= 2;
		} else {
			L /= 2;
			R /= 2;
		}

		lead += total / 2;
		total /= 2;
	}

	return (1ll<<N) - lead;
}

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++) {
		scanf("%d%lld", &N, &P);
		
		long long lower = 0, upper = (1ll<<N);
		while(lower + 1 < upper) {
			long long mid = (lower + upper) / 2;
			if(worst(mid) <= P) lower = mid;
			else upper = mid;
		}
		X = lower;

		lower = 0, upper = (1ll<<N);
		while(lower + 1 < upper) {
			long long mid = (lower + upper) / 2;
			if(best(mid) <= P) lower = mid;
			else upper = mid;
		}
		Y = lower;

		printf("Case #%d: %lld %lld\n", test, X, Y);
	}
	return 0;
}
