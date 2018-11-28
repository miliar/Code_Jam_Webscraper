#include <iostream>
#include <cstdio>
#include <cstring>
#include <cassert>

using namespace std;

static int N[1001];
static int M[1001];

int f()
{
	int temp;
	int min = 10000;
	int n;
	for(int i = 1; i < 1001; i++) {
		for(int j = i; j < 1001; j++) {
			temp = j / i;
			if(j % i == 0) temp--;
			temp *= N[j];
			M[i] += temp;
		}
		if(min > i + M[i]) {
			min = i + M[i];
			n = i;
		}
	}
	return min;
}

int main()
{
	int T;
	int D, P;
	assert(scanf("%d", &T));
	for(int i = 0; i < T; i++) {
		memset(N, 0, sizeof(N));
		memset(M, 0, sizeof(M));
		assert(scanf("%d", &D));
		for(int j = 0; j < D; j++) {
			assert(scanf("%d", &P));
			N[P]++;
		}

		cout<<"Case #"<<i+1<<": " <<f()<<endl;
	}
}
