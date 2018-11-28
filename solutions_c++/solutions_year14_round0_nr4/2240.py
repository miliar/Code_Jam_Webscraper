#include <stdio.h>
#include <set>
#include <algorithm>

using namespace std;

long double Naomi[1000+100];
set <long double> S1;
set <long double> S2;
set <long double>::iterator it;

void Wczytaj(int n){
	int i;
	long double liczba;
	for(i=0; i<n; i++) scanf("%Lf", &Naomi[i]);
	for(i=0; i<n; i++){
		scanf("%Lf", &liczba);
		S1.insert( liczba );
		S2.insert( liczba );
	}
}

int main(){
	int t,j,n,n_point,i;
	scanf("%d", &t);
	for(j=0; j<t; j++){
		S1.clear();
		S2.clear();
		scanf("%d", &n);
		Wczytaj(n);
		sort(Naomi,Naomi+n);
		for(i=0; i<n; i++){
			it = S1.lower_bound( Naomi[i] );
			if( it != S1.end() ) S1.erase( it );
		}
		n_point = 0;
		for(i=0; i<n; i++){
			it = (S2.end());
			it--;
			if( *it < 1 ){
				//printf("WOW\n");
				if( Naomi[i] > *(S2.begin()) ){
					//printf("%Lf\n", *it);
					n_point++;
					S2.erase( S2.begin() );
				}
				else{
					//printf("%Lf 1 \n", *it);
					S2.erase( it );
				}
			}
			else{
				S2.erase( it );
			}
		}
		printf("Case #%d: %d %d\n", j+1,n_point,S1.size());
	}
	return 0;
}
