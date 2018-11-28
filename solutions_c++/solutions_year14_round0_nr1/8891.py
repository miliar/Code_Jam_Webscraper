#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
	fstream plik, plikout;
	plik.open("a.in", ios::in);
	plikout.open("a.out", ios::out);
	int n;
	plik >> n;
	int tab1[4][4];
	int tab2[4][4];
	int k1, k2;
	for (int i = 0; i < n; i++){
		plikout << "Case #" << i + 1 << ": ";
		//wczytywanie
		plik >> k1;
		for (int j = 0; j < 16; j++){
			plik >> tab1[j / 4][j % 4];
		}
		plik >> k2;
		for (int j = 0; j < 16; j++){
			plik >> tab2[j / 4][j % 4];
		}
		cout << tab2[3][0] << endl;

		//czy ochotnik oszukal
		bool prawda = false;
		int powtorki = 0;
		int liczba;
		for (int j = 0; j < 4; j++){//tablica 1
			for (int t = 0; t < 4; t++){
				if (tab1[k1-1][j] == tab2[k2-1][t]){
					prawda = true;
					powtorki++;
					liczba = tab1[k1-1][j];
				}
			}
		}
		if (!prawda){
			plikout << "Volunteer cheated!" << endl;
		}else if (powtorki > 1){
			plikout << "Bad magician!" << endl;
		}
		else{
			plikout << liczba << endl;
		}

	}
	system("pause");
	plik.close();
	plikout.close();
}