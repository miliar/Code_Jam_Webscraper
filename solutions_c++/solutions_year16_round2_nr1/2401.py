// GCJ20161BA.cpp 
//


#include <istream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>

#define pb(x) push_back(x)
#define ll long long

using namespace std;

ifstream *fi;
FILE *fo;


void Run() {
	int i, j, k, m,n,  a,b,tc,mn,nb,kmn,aa,bb,lg,lw,lc;
	int T;
	int res,N;
	int nblet[26],nbchif[10];
	double dres;
	string st,sres,S;
	char c;
	vector <vector <int> > ht, htr;
	vector <int> vres,lico[2];
	string schif[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int ordchif[10]={6,8,0,2,3,4,5,7,9,1};
	string ordst="XGZWHRFVIN";
	int h[2501];
	
	
	// Init Tout début
	
	
	// Lecture début
	*fi >> T;

	// getline(*fi, st); // Pour terminer la ligne
	// getline(*fi, st); // Pour lire une chaîne de caractères
	
	// Parcours des N test cases :
	
	getline(*fi, st);  // Pour passer à la ligne suivante :
	for (tc = 1; tc <= T; tc++) {
		
		// Reset du tour précédent (dont vectors) !
		sres="";
		for(i=0;i<26;i++) nblet[i]=0;
		for(i=0;i<10;i++) nbchif[i]=0;
		
		// Init
		*fi >> st ;
		//getline(*fi, st);  // Pour lire une ligne !
		nb=st.size();
		for(i=0;i<nb;i++) nblet[st[i]-'A']++;

		// Exe
		for(i=0;i<10;i++){
			k=ordchif[i];
			n=nblet[ordst[i]-'A'];
			nbchif[k]=n;
			for(j=0;j<schif[k].size();j++) nblet[schif[k][j]-'A']-=n;			
		}
		
		for(i=0;i<10;i++)
			for(j=0;j<nbchif[i];j++)
				sres+=(char)(i+'0');
		

		// Sortie
		fprintf(fo, "Case #%d: %s\n", tc,sres.c_str());
		printf("Case #%d: %s\n", tc,sres.c_str());
	}
}


bool Fichiers() {
	string s;
	s="A-large.in";
	printf("Fichier d'entrees ->    %s    <-\n",s.c_str());
	fi=new ifstream(s.c_str());
	if(!(*fi).good()) {
		printf("Pb ouverture du fichier d'entrees %s\n",s.c_str());
		return false;
	}
	fo=fopen("Test.out","w");
	return true;
}


int main(int argc, char** argv) {
	unsigned int i;

	printf("GCJ20161BA\n");
	if(!Fichiers()) return 1;
	Run();


	return 0;
}