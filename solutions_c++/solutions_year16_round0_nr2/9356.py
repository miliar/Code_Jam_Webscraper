#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;


int Wypisz(int n, string Wczytaj){
	int i, wynik;
	wynik=0;
	for(i=1; i<n; i++){
		if(Wczytaj[i]!=Wczytaj[i-1]){
			wynik++;
		}
	}
	if(Wczytaj[n-1]=='-'){
		wynik++;
	}
	return wynik;
}

int main (){
	int n, t, i, x;
	string Wczytaj;
	scanf("%d", &t);
	x=1;
	for(i=1; i<=t; i++){
		cin >> Wczytaj;
		n=Wczytaj.size();
		printf("Case #%d: %d\n", x, Wypisz(n, Wczytaj) );
		x++;
	}
	return 0;
}
