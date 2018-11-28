#include <cstdio>
#include <algorithm>

using namespace std;

pair <long long,long long> K[20];
long long L[20];

int main(){
	int t,i,j,k,l,n,m;
	long long wsk,pot,wynik,n_wynik,suma,licznik;
	bool czy;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		n_wynik = 1e9;
		n_wynik *= n_wynik;
		scanf("%d", &n);
		suma = 0;
		if(n%10 == 0){
			n--;
			suma++;
		}
		j = 0;
		for(k=0; k<20; k++) K[k].first = K[k].second = 0;
		while(n>0){
			L[j++] = n%10;
			n /= 10;
		}
		if(j!= 1) L[j-1]--;
		pot = 1;
		licznik = 10;
		wsk = 9;
		for(k=0; k<j-1; k++){
			suma += licznik;
			if(k%2 == 1) wsk *= 10;
			licznik += wsk;
		}
		for(k=0; k<j; k++){
			K[k].first = L[k]*pot;
			pot *= 10;
		}
		pot = 1;
		for(k=j-1; k>=0; k--){
			K[k].second = L[k]*pot;
			pot *= 10;
		}
		//for(k=0; k<j; k++) printf("%lld %lld\n", K[k].first, K[k].second);
		for(k=0; k<(1<<j); k++){
			wynik = 0;
			czy = false;
			for(l=0; l<j; l++){
				if( k & (1<<l) ) wynik += K[l].first;
				else {
					wynik += K[l].second;
					czy = true;
				}
			}
			if(czy) wynik++;
			n_wynik = min(wynik, n_wynik);
		}
		printf("Case #%d: %lld\n", i+1,n_wynik+suma);
	}
	return 0;
}
