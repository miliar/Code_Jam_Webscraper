#include <cstdio>
#include <algorithm>
using namespace std;

double c,f,x,p[100100];

int t,test;

void solve() {
	test++;
	printf("Case #%d: ",test);
	
	scanf("%lf %lf %lf",&c,&f,&x);
	
	double sol = 1000000;
	
	p[0] = 0;
	for (int i = 1;i < 100010; i++)
		p[i] = c / (double)(max((double)(i - 1) * f, (double)0) + 2) + p[i - 1];
	
	/*for (int i = 0;i < 11; i++)
		printf("%.6lf ",p[i]);
	printf("\n");
	*/
	for (int i = 0;i < 100010; i++) 
		sol = min(sol, p[i] + (x / ((double)i * f + 2)));
	
	printf("%.6lf\n",sol);}
		
		
int main() {
	scanf("%d",&t);
	while (t--) solve();
	
	return 0;}
