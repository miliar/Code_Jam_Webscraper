#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void stampa(const int ris, const int i, ofstream &OUT)
{
	if(ris==0) OUT<<"Case #" <<i <<": INSOMNIA\n";
	else OUT <<"Case #" <<i <<": "<<ris<<'\n';
	return;
}

bool check(bool* S)
{
	
	for(int i=0; i<10; i++)
	{
		if(S[i]==false) return false;
	}
	
	// se esco dal ciclo, S[i]==true per ogni i, quindi ho trovato tutti i valori
	return true;
}


void segna(bool*S, int ris)
{
	
	//per ogni cifra, segna su B se cella corrisp e` ancora 0
	//a ogni ciclo cancello una cifra; quando resto con 0 esco
	while(ris>0)
	{
		int l=ris%10; // prendi ultima cifra; 0<=l<=9
		if(S[l]==0) S[l]=true; //segna
		ris= ris/10; // cancella ultima cifra
	}
	
}

// PRE:
void test(const int N, const int i, ofstream &OUT)
{
	bool S[10]={}; //segno cifre
	int ris=N; // ini ris

	// caso '0' : 0*N=0 : INSONNIA
	if(N==0)
	{
		stampa(ris,i,OUT);
		return;
	}
		

	
	// caso : default
	bool exit=false;
	// R: se S e` stato completato=> exit=true, stampo&&esco
	//		se no, continuo con +N
	// a ogni inizio ciclo ho controllato S per ris-N
	while(exit==false)
	{
		
		// segno S con ris
		segna(S,ris);
		
		//controllo cifre su S
		if( check(S)==true) // ho trovato tutte le cifre
		{
			stampa(ris,i,OUT);
			exit=true;
		}
		// incremento +N
		ris= ris+N;

	}	//POST: exit==true =>	S completato, torno nel main
	return;
	
}





main(){

ifstream IN("input");
ofstream OUT("output");
if(IN&&OUT)
{
	int T,N;
	IN>>T; // # test

	for(int i=1; i<=T; i++)
	{
		// test #T
		IN>>N; 
		test(N,i,OUT);
	}
	
}
else OUT<<"errore files\n";


}//END
