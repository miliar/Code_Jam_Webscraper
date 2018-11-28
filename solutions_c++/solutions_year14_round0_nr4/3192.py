#include <cstdio>
#include <cmath>
#include <algorithm>
const int MAX = 1000;
double na[MAX];
double ken[MAX];
int T, N;
using namespace std;
int war(){
	int j = 0;//ken's idx
	for (int i = 0; i < N; i++) {//invariant: j not used
		while (j < N && ken[j] < na[i]) {
			j++;
		}
		if(j >= N) return N-i;
		j++;
	}
	return 0;
}
int dwar(){
	int j = 0;//na's idx
	for (int i = 0; i < N; i++) {//invariant: j not used
		while (j < N && na[j] < ken[i]) {
			j++;
		}
		if(j >= N) return i;
		j++;
	}
	return N;
}
int main(int argc, const char *argv[])
{
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d", &N);
		for (int j = 0; j < N; j++) scanf("%lf", &na[j]);
		for (int j = 0; j < N; j++) scanf("%lf", &ken[j]);
		sort(na, na+N);	
		sort(ken, ken+N);	
		int res2 = war();
		int res1 = dwar();
		printf("Case #%d: %d %d\n", i, res1, res2);
	}
	return 0;
}
