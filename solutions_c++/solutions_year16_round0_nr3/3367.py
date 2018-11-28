#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
typedef long long LL;
using namespace std;
int n = 16;
int a[59];
bool isp(LL x) {
	for (LL i = 2; i * i <= x; i ++)
		if (x % i == 0)
			return false;
	return true;
}
bool ck() {
	for (int i = 2; i <= 10; i ++) {
		LL t = 1, z = 0;
		for (int j = 1; j <= n; j ++) {
			z = z + a[j] * t;
			t = t * i;
		}
		if (isp(z))
			return false;
	}
	return true;
}
int outp(LL x) {
	for (LL i = 2; i * i <= x; i ++)
		if (x % i == 0)
			return i;
}
void print() {
	for (int j = n; j >= 1; j --)
		printf("%d", a[j]);
	for (int i = 2; i <= 10; i ++) {
		LL t = 1, z = 0;
		for (int j = 1; j <= n; j ++) {
			z = z + a[j] * t;
			t = t * i;
		}
		printf(" %d", outp(z));
	}
	printf("\n");
}
int sum = 0;
void DFS(int dep) {
	if (sum >= 50) return ;
	if (dep == n) {
		if (ck())
			print(), sum++;
		return ;
	}
	a[dep] = 1;
	DFS(dep + 1);
	a[dep] = 0;
	DFS(dep + 1);
} 
int main ()
{
	freopen("a.out", "w", stdout);
	printf("Case #1: \n");
	a[1] = a[n] = 1;
	DFS(2);
	return 0;
}

