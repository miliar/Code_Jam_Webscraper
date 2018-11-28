#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int GCD(int a, int b)
{
	  if (a == b) return a;
	    else if (a > b) return GCD(a-b, b);
		  else return GCD(a, b-a);
}

int LCM(int a, int b)
{
	  return a * b / GCD(a, b);
}

int M[1001];
int served[1001];
int solve(int b, int c) {
	int ret;
	// lcm calculate
	int lcm = M[0];
	for (int i = 0; i < b; i++) {
		lcm = LCM(lcm, M[i]);
	}

	int lcm_customer = 0;
	for (int i = 0; i < b; i++) {
		lcm_customer += (lcm / M[i]);
	// 	printf("lcd %d\n", lcm / M[i]);
	}
	// printf("customer %d\n", lcm_customer);
	c = lcm_customer + (c % lcm_customer);
	// printf("%d\n", c);

	for(int i = 0; i < b; i++) {
		served[i] = 0;
	}

	for (int i = 0; i < c; i++) {
		for(int j = 0; j < b; j++) {
			if (served[j] == 0) {
				served[j] = M[j];
				ret = j;
				break;
			}
		}
		int mini = served[0];
		for(int j = 0; j < b; j++) {
			mini = min(mini, served[j]);
		}
		// printf("mini %d\n", mini);
		for(int j = 0; j < b; j++) {
			served[j] = served[j] - mini;
		}

	}

	/*
	for(int i = 0; i < b; i++) {
		served[i] = 0;
	}

	while(1) {
		for (int i = 0; i < b; i++) {
			if (served[i] == 0) {
				served[i] = M[i];
				c--;
				ret = i;
			}
			if (c == 0)
				break;
		}
		if (c == 0)
			break;
		
		for(int i = 0; i < b; i++) 
			served[i]--;
	}
	*/

	return ret + 1;
}

int main() {
	int t;
	cin >> t;

    for (int i = 1; i <= t; i++) {
		int b; cin >> b;
		int c; cin >> c;
		for(int j = 0; j < b; j++) {
			cin >> M[j];
		}
    	printf("Case #%d: %d\n", i, solve(b, c));
    }

	return 0;
}
