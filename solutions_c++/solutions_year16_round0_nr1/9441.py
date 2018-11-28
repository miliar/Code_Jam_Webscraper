/*
 * a.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: aki
 */
#include<cstdlib>
#include<cstdio>
#include<cmath>
bool cifre[10];

void rastaviteNaCifre(double br){
	while(br>0){
		double cifra=fmod(br, 10.0);
		int c = (int)cifra;
		cifre[c]=true;
		br=floor(br/10);
	}
}
bool proveriteCifre(){
	for(int i=0;i<10;i++)
		if(!cifre[i])return false;
	return true;
}


int main(){
	freopen("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int T, t;
	scanf("%d\n", &T);
	T++;


	for(t=1;t<T;t++){

		double rez, i=2, N, pom;
		long int k;
		for(int inicc=0;inicc<10;inicc++)
			cifre[inicc]=false;
		scanf("%d\n",&k);
		N=(double)k;
		rastaviteNaCifre(N);
		rez = N*i;pom=N;

		while(floor(rez)>floor(pom)){
			rastaviteNaCifre(rez);
			if (proveriteCifre())break;
			pom=rez;
			rez=N*(++i);
		}
		if(floor(rez)<=floor(N))printf("Case #%d: INSOMNIA\n",t);
		else
			printf("Case #%d: %.0f \n",t,rez);
	}

}



