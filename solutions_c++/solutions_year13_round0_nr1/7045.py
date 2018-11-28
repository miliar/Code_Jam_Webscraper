#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool czyPrzekatne(char plansza[4][4], char znak){

	int ilePrzekatna1=0;
	int ilePrzekatna2=0;

	for(int j=0;j<4;j++){
		if(plansza[j][j]!=znak&&plansza[j][j]!='T'){
			ilePrzekatna1=0;
		}else{
			ilePrzekatna1++;
			if(ilePrzekatna1==4) return true;
		}

		if(plansza[j][3-j]!=znak&&plansza[j][3-j]!='T'){
			ilePrzekatna2=0;
		}else{
			ilePrzekatna2++;
			if(ilePrzekatna2==4) return true;
		}
	}
	return false;
}

bool czyLiniaZnakow(char plansza[4][4],  char znak){
	int ileWiersz=0;
	int ileKolumna=0;

	for(int nr=0;nr<4;nr++){
		for(int j=0;j<4;j++){
			if(plansza[nr][j]!=znak&&plansza[nr][j]!='T'){
				ileWiersz=0;
			}else{
				ileWiersz++;
				if(ileWiersz==4) return true;
			}

			if(plansza[j][nr]!=znak&&plansza[j][nr]!='T'){
				ileKolumna=0;
			}else{
				ileKolumna++;
				if(ileKolumna==4) return true;
			}
		}
		ileWiersz=0;
		ileKolumna=0;
	}
	return false;
}
bool czyRemis(char plansza[4][4]){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(plansza[i][j]=='.')
				return false;
		}
	}
	return true;
}
bool czyWygral(char plansza[4][4], int *kto){
	for(int i=0; i<4;i++){
		if(czyLiniaZnakow(plansza, 'X')||czyPrzekatne(plansza, 'X')){
			*kto=1;
			return true;
		}

		if(czyLiniaZnakow(plansza, 'O')||czyPrzekatne(plansza, 'O')){
			*kto=2;
			return true;
		}
	}
	return false;
	//zwraca true, jesli ktos wygral
	//zwraca false, jesli nie wiadomo
}

string jakiWynik(char plansza[4][4]){
	string wynik;
	int kto=0;

	//wyswietlanie dla sprawdzenia
	//cout<<endl;
	//for(int i=0;i<4;i++){
	//	for(int j=0;j<4;j++){
	//		cout<<"plansza "<<j<<", 0: "<<plansza[i][j]<<endl;
	//	}
	//	cout<<endl;
	//}

	//sprawdzenie czy gra jest zakonczona i kto wygral
	if(czyWygral(plansza, &kto)){
		if(kto==1){ //wygral X
			wynik="X won";
		}
		if(kto==2){ //wygral O
			wynik="O won";
		}
	}else{//nikt nie wygral, sprawdzamy dalej

		//sprawdzenie czy jest remis
		if(czyRemis(plansza)){
			wynik="Draw";
		}else{
			//inaczej gra nieroztrzygnieta
			wynik="Game has not completed";
		}
	}

	//cout<<wynik;
	return wynik;
}

int main(){

	ofstream plikOutput("C:/Users/Kara/Desktop/plik2.in");
	ifstream plikInput("C:/Users/Kara/Desktop/A-large.in");//A-small-attempt0
	string wczytane;
	int T;
	int caseNr=1;
	int k=0;
	char *linia = new char[4];
	char plansza[4][4]; //zawiera w sobie jedna gre


	//OTWIERANIE PLIKOW
	if(!plikInput.is_open()){
		cout<<"Nie otworzono pliku z inputem!\n"<<endl;
		return 1;
	}
	if(!plikOutput.is_open()){
		cout<<"Nie otworzono pliku do zapisu!\n"<<endl;
		return 1;
	}

	//WCZYTYWANIE Z PLIKU
		
		getline(plikInput,wczytane);
		T=atoi(wczytane.c_str());

		while(!plikInput.eof()&&caseNr<=T){

			//zerujemy talblice linii
			linia[0]=' ';
			linia[1]=' ';
			linia[2]=' ';
			linia[3]=' ';

			//wczytujemy linie z pliku i kopiujemy do linii
			getline(plikInput,wczytane); 
			strcpy(linia, wczytane.c_str()); 

			//wyswietlamy linie dla sprawdzenia
			//for(int i=0;i<4;i++){
			//	cout<<linia[i];
			//}
			//cout<<endl;

			//jesli wczytamy punta linie, przechodzimy dalej
			if(linia[3]==' ')
				continue;

			//zapisujemy dane do planszy - k-ty wiersz, kolumny 1-4
			plansza[k][0]=linia[0];
			plansza[k][1]=linia[1];
			plansza[k][2]=linia[2];
			plansza[k][3]=linia[3];


			//wyswietlamy chary w planszy dla sprawdzenia
			//cout<<"plansza "<<k<<", 0: "<<plansza[k][0]<<endl;
			//cout<<"plansza "<<k<<", 1: "<<plansza[k][1]<<endl;
			//cout<<"plansza "<<k<<", 2: "<<plansza[k][2]<<endl;
			//cout<<"plansza "<<k<<", 3: "<<plansza[k][3]<<endl;

			//sprawdzamy jaki wynik oraz zmieniamy wiersz na ktorym dzialamy lub rozpoczynamy nowa rozgrywke
			if(k==3){
				//ZAPISYWANIE DO PLIKU
				plikOutput<<"Case #"<<caseNr<<": "<<jakiWynik(plansza)<<endl;
				caseNr++;
				k=0;
			}else{
				k++;
			}
		}

	plikInput.close();
	plikOutput.close();

}