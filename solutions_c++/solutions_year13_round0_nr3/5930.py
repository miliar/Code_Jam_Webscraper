#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string>

using namespace std;

bool czyPalindrom(int liczba){
	int ilCyfr=int(log10(double(liczba)))+1;
	int iterator=1;
	//string slowo;
	//char *slowoc = new char[10000000];
	//sprintf(strcpy(slowoc,slowo.c_str()), "%d", i);
	//int ilCyfr = strlen(slowoc);

	if(ilCyfr==1){
		return true;
	}
	if(ilCyfr==2){
		int dziesiatki=liczba/10;
		int jednosci=liczba%10;
		if(dziesiatki==jednosci){
			return true;
		}else{
			return false;
		}
	}

	while(iterator<=(int)(ilCyfr/2)){
	int lewaCyfra=0;
	int prawaCyfra=0;

	if(iterator==1){
		lewaCyfra=(int)(liczba/pow(10.0,ilCyfr-iterator));
		prawaCyfra = liczba%10;
	}else{
		lewaCyfra = int(liczba%(int)pow(10.0,ilCyfr-iterator+1)/pow(10.0,ilCyfr-iterator));
		prawaCyfra = int(liczba%(int)pow(10.0,iterator)/pow(10.0,ilCyfr-iterator-1));
	}
	if(!lewaCyfra==prawaCyfra) return false;
	iterator++;
	}

	return true;
}

int main(){

	ofstream plikOutput("C:/Users/Kara/Desktop/wynikC.in");
	ifstream plikInput("C:/Users/Kara/Desktop/C-small-attempt0.in");
	string wczytane;
	int T;
	int caseNr=1;
	int A;
	int B;
	int wynik=0;


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

		//wczytujemy przedzialy
		plikInput>>A;
		plikInput>>B;

		//wyswietlamy linie dla sprawdzenia
		//cout<<A<<" "<<B<<" "<<endl;

		for(int i=A; i<=B;i++){
			double sqi=0.0; 
			//sprawdzamy czy liczba jest palindromem
			
			if(czyPalindrom(i)){
				sqi=sqrt((double)i); 
				if(int(sqi)!=sqi){ //jesli tak, sprawdzamy czy jej pierwiastek jest liczba calkowita
					continue;
				}
				if(czyPalindrom(sqi)){ //sprawdzamy czy pierwiastek jest palindromem
					wynik++;
				}
			}
		}

		//ZAPISYWANIE DO PLIKU
				plikOutput<<"Case #"<<caseNr<<": "<<wynik<<endl;
				caseNr++;
				wynik=0;
	}

	plikInput.close();
	plikOutput.close();

}