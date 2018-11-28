#include<iostream>
#include<cstdio>

using namespace std;

int Tablica[15];

void Dodaj(int n, int &rozne){
	int reszta;
	while(n>0){
		reszta=n%10;
		if(Tablica[reszta]==0){
			Tablica[reszta]=1;
			rozne++;
		}
		n/=10;
	}
}

int Wypisz(int n){
	int rozne, pocz;
	rozne=0;
	pocz=n;
	while(rozne<10){
		Dodaj(n, rozne);
		n+=pocz;
	}
	n-=pocz;
	for(int i=0; i<=10; i++){
		Tablica[i]=0;
	}
	return n;
}

int main (){
	int n, t, i, x;
	scanf("%d", &t);
	x=1;
	for(i=1; i<=t; i++){
		scanf("%d", &n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n", x );
			x++;
			continue;
		}
		printf("Case #%d: %d\n", x, Wypisz(n) );
		x++;
	}
}
