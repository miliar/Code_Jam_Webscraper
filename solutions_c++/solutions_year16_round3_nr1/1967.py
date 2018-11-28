// GCJ20161CA.cpp 
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
	int i, j, k, m,n,  a,b,tc,mn,nb,kmn,aa,bb,lg,lw,lc,som;
	int T;
	int res,N;
	double dres;
	string st,sres,S;
	char c;
	vector < vector <int> > nbs,nbs2;
	int h1,h2,mx1,mx2,mx3;
	
	
	// Init Tout début
	
	
	// Lecture début
	*fi >> T;

	// getline(*fi, st); // Pour terminer la ligne
	// getline(*fi, st); // Pour lire une chaîne de caractères
	
	// Parcours des N test cases :
	
	getline(*fi, st);  // Pour passer à la ligne suivante :
	for (tc = 1; tc <= T; tc++) {
		
		// Reset du tour précédent (dont vectors) !
		nbs.clear();
		nbs2.clear();
		res=0;
		
		// Init
		*fi >> N ;
		//getline(*fi, st);  // Pour lire une ligne !
		for(i=0;i<N;i++) {
			*fi >> a ;
			nbs.pb(*(new vector <int>));
			nbs[i].pb(a);
			nbs[i].pb(i);
		}
		
		som=0;
		for(i=0;i<N;i++) som+=nbs[i][0];

		// Exe
		fprintf(fo, "Case #%d:", tc);
		printf("Case #%d:", tc);
		do {
			sort(nbs.begin(),nbs.end());
			if(som==2) {
				fprintf(fo, " %c%c", 'A'+nbs[N-1][1],'A'+nbs[N-2][1]);
				printf(" %c%c", 'A'+nbs[N-1][1],'A'+nbs[N-2][1]);
				break;
			} 
			if(som==3) {
				fprintf(fo, " %c", 'A'+nbs[N-1][1]);
				printf(" %c", 'A'+nbs[N-1][1]);
				nbs[N-1][0]--;
				som--;
				continue;
			} 
			fprintf(fo, " %c%c", 'A'+nbs[N-1][1],'A'+nbs[N-2][1]);
			printf(" %c%c", 'A'+nbs[N-1][1],'A'+nbs[N-2][1]);
			nbs[N-1][0]--;
			nbs[N-2][0]--;
			som-=2;
		} while (true);
		

		// Sortie
		fprintf(fo, "\n");
		printf("\n");
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

	printf("GCJ20161CA\n");
	if(!Fichiers()) return 1;
	Run();


	return 0;
}