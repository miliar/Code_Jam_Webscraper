#include <stdio.h>
#define MIN(a,b) ((a<b)?a:b)
using namespace std;
double c, f, x;
int main(){
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){
		printf("Case #%d: ", ind);
		scanf("%lf %lf %lf", &c, &f, &x);
		double s1, s2;
		int i = 1;
		s1 = c/2; s2 = x/2;
		while(s1+x/(2+i*f)<s2){
			s2 = s1+x/(2+i*f);
			s1 = s1+c/(2+i*f);
			i++;
		}
		printf("%.7lf\n", s2);
	}
	return 0;
}