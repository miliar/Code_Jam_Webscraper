#include <iostream>
#include <cmath>
using namespace std;

double temp;
long long int T;
int Z, N, B, M[1001];

long long int notInLine (long long int T) {
	long long int ans = 0;
	for (int i = 1 ; i <= B ; i++)
		ans += ceil (1.0*T/M[i]);
	return ans;
}

int main() {
	scanf ("%d", &Z);
	for (int z = 1 ; z <= Z ; z++) {
		
		temp = 0;
		scanf ("%d%d", &B, &N);
		for (int i = 1 ; i <= B ; i++) {
			scanf ("%d", &M[i]);
			temp += 1.0/M[i];
		}
		T = floor ((N-1)*1.0/temp);
		
		while (notInLine (T) > N-1) T--;
		long long int x = notInLine (T)+1;
		int i = 0;
		while (x <= N) {
			i++;
			while (T % M[i] != 0)
				i++;
			x++;
		}
		printf ("Case #%d: %d\n", z, i); 
	}
	return 0;
}