#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string>

using namespace std;

int ileFarbyPoszlo(int n){

	//n^2-(n-1)^2
	//n^2- (n^2-2n+1)
	//n^2- n^2+2n-1
	//czarna farba dla ntego promienia
	return 2*n-1;
}

int main(){

	ofstream plikOutput("C:/Users/Kara/Desktop/wynikA.in");
	ifstream plikInput("C:/Users/Kara/Desktop/A-small-attempt1.in");
	string wczytane;
	int T;
	int caseNr=1;
	int promien;
	int promienT;
	int farby;
	int zuzyto=0;
	int okregow=0;


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
	cout<<T<<endl;

	while(!plikInput.eof()&&caseNr<=T){

		//wczytujemy przedzialy
		plikInput>>promien;
		plikInput>>farby;
		promienT=promien;

		//promien^2 milimetrow farby
		//farby-=(promien+1)*(promien+1)-promien*promien;
		do{
			zuzyto+=ileFarbyPoszlo(promienT+1);
			 //malowanie okregow
			promienT+=2; //nast czarny okrag
			if(farby>=zuzyto) okregow++;
		}while(farby>zuzyto||promienT<promien);

		plikOutput<<"Case #"<<caseNr<<": "<<okregow<<endl;
		caseNr++;
		okregow=0;
		zuzyto=0;
	}

	plikInput.close();
	plikOutput.close();

	return 0;
}