#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int t,i,j;
	long double c,f,x,wynik,per_sec,ile_minelo;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		scanf("%Lf%Lf%Lf", &c,&f,&x);
		per_sec = 2;
		wynik = x/per_sec;
		ile_minelo = 0;
		for(j=1; j<=x*100; j++){
			ile_minelo += c/per_sec;
			per_sec += f;
			wynik = min(wynik,ile_minelo+x/per_sec);
		}
		printf("Case #%d: %.7Lf\n", i+1,wynik);
	}
	return 0;
}
