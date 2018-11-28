// GCJ20161AA.cpp 
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
	int i, j, k, m,  a,b,tc,mn,nb,kmn,aa,bb,lg,lw;
	int T;
	int res;
	int pt;
	double dres;
	string st,sres,S,sl,sr;
	char c,cmax;
	
	
	// Init Tout début
	
	
	// Lecture début
	*fi >> T;

	// getline(*fi, st); // Pour terminer la ligne
	// getline(*fi, st); // Pour lire une chaîne de caractères
	
	// Parcours des N test cases :
	
	getline(*fi, st);  // Pour passer à la ligne suivante :
	for (tc = 1; tc <= T; tc++) {
		
		// Reset du tour précédent (dont vectors) !
		res=0;
		sres="";
		
		// Init
		*fi >> S ;
		//getline(*fi, st);  // Pour lire une ligne !
		nb=S.size();
		a=0;
		b=nb-1;
		sl="";
		sr="";
		
		// Exe
		while(b>=0) {
			cmax='A'-1;
			for(i=b;i>=a;i--) {
				if(S[i]>cmax) {
					k=i;
					cmax=S[i];
				}
			}
			sl=sl+S[k];
			if(k!=b) sr=S.substr(k+1, b-k)+sr;
			b=k-1;
		}
		sres=sl+sr;

		// Sortie
		fprintf(fo, "Case #%d: %s\n", tc,sres.c_str());
		printf("Case #%d: %s\n", tc,sres.c_str());
	}
}


void Fichiers() {
	fi=new ifstream("A-large.in");
	fo=fopen("Test.out","w");
}


int main(int argc, char** argv) {
	unsigned int i;

	printf("GCJ20161AA\n");
	Fichiers();
	Run();


	return 0;
}