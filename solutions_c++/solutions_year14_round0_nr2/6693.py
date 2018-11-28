#include<cstdio>
using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i){
		double c, f, x, s = 2, vysledok = 0;
		scanf("%lf %lf %lf", &c, &f, &x);
		while(((c / s) + (x / (s+f))) < (x / s)){
			vysledok += (c / s);
			s += f;
		}
		vysledok += (x / s);
		printf("Case #%d: %.7f\n", i + 1, vysledok);
	}
	return 0;
}
