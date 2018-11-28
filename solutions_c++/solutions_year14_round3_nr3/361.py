#include <cstdio>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string>

using namespace std;

int n, m, k;
/*
void wypisz(bool tab[][2]) {
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cout<< tab[i][j];
		}
		cout<<endl;
	}
}
*/
int main() {
	
	int cases;
	cin >> cases;
	
	for(int case_number=1; case_number <= cases; case_number++) {
		
		cin >> n >> m >> k;
		
		int wynik = 0;
		
		if(!(n > 2 && m > 2 && k > 4)) {
			wynik = 0;
		}
		else if(k >= (n*m) -4) {
			wynik = (n-2) * (m-2);
		}
		else {
			bool tab [n][m];	
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					tab[i][j] = false;
				}
			}
			
			int zakryte =0;
			int x=0, y=0; //aktualne wsp
			int x_wolny=0, y_wolny=0;
			//krok 1 -  X
			tab[0][1] = true;
			tab[1][0] = true;
			tab[1][1] = true;
			tab[1][2] = true;
			tab[2][1] = true;
			zakryte=5;
			wynik++;
			
			x=2; y=1;
			x_wolny=2; y_wolny=2;
			
			// krok 2 - po przekatnych
			while(k-zakryte > 2 && x+1 < n && y+1 < m) {
					y++; //jeden w dol
					tab[x][y] = true;
					tab[x][y+1] = true;
					x++; // jeden w prawo
					tab[x][y] = true;
					zakryte +=3;
					wynik++;
			}
			
			if(k-zakryte < 3 && x<n-1 && y < m-2) zakryte +=2;
			
			while(zakryte < k) {
				
				if(n>m) {
					x=x_wolny;
					y=0;
					x_wolny++;
					
					tab[x][y]=true;
					zakryte++;
					
					while(zakryte < k && y < m-3) {
						x++; y++; //w dol w prawo
						tab[x][y] = true;
						zakryte++;
						wynik++;
					}
					if(x < n-1 && zakryte <= k-2) {
						x++; y++;
						tab[x][y] = true;
						zakryte++;
						tab[x-1][y+1] = true;
						zakryte++;
						wynik++;
					}
				}
				else {
					y=y_wolny;
					x=0;
					y_wolny++;
					
					tab[x][y]=true;
					zakryte++;
					
					while(zakryte < k && x < n-3) {
						x++; y++; //w dol w prawo
						tab[x][y] = true;
						zakryte++;
						wynik++;
					}
					
					if(y < m-1 && zakryte <= k-2) {
						x++; y++;
						tab[x][y] = true;
						zakryte++;
						tab[x+1][y-1] = true;
						zakryte++;
						wynik++;
					}
				}
				
			/*
				for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					cout<< tab[i][j];
				} cout<<endl; } cout << endl;
				*/
				//zakryte+=100;
			}
		}
		
		wynik = k - wynik;
		
		cout << "Case #" << case_number << ": " << wynik << endl;
	}
	
	return 0;
}
