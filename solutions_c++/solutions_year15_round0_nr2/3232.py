#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>

int solve(int *P, int Pmax, int Ptotal, int D) {

    int Ts = (int) std::sqrt((double)Ptotal / D);
    //int Ts = 1;
    int min = INT_MAX;

    for (; Ts <= Pmax; ++Ts) {

	int sum = 0;
	int max = 0;

	for (int i = Ts+1; i<= Pmax; ++i) {
	    if (P[i] > 0) {
	        int n = P[i];
	        int N = (i + Ts - 1) / Ts;
	        int R = (i + N - 1) / N;
	        sum += n * (N - 1);
	        max = std::max(max, R);
	    }
	}

	for (int i = max+1; i <= Ts; ++i) {
	    if (P[i] > 0) {
		max = i;
	    }
	}

	min = std::min(min, sum+max);
    }

    return min;
}

int main() {

    int T;
    scanf("%d", &T);
    for (int i=0; i<T; ++i) {
        
	int D;
	scanf("%d", &D);
	int Pmax = 0;
	int Ptotal = 0;
	int P[1001] = {0,};

	for (int i=0; i<D; ++i) {
	    
	    int p;
	    scanf("%d", &p);
	    ++P[p];
	    Pmax = std::max(Pmax, p);
	    Ptotal += p;
        }

	printf("Case #%d: %d\n", i+1, solve(P, Pmax, Ptotal, D));
    }

    return 0;
}
