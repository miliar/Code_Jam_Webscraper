#include <cstdio>

using namespace std;

const int TAILLE = 4;

int grille[TAILLE][TAILLE];

int possibles[TAILLE];

int rempliPoss(int lin){
	for(int iCol=0; iCol<TAILLE; iCol++)
		possibles[iCol]=grille[lin][iCol];
}

int soluce(int lin){
	int solution = -1;
	for(int iCol=0; iCol<TAILLE; iCol++)
		for(int iPoss = 0; iPoss<TAILLE; iPoss++)
			if(possibles[iPoss]==grille[lin][iCol]){
				if(solution==-1)
					solution = grille[lin][iCol];
				else
					return -2;
			}
	return solution;
}

void lireGrille(){
	for(int iLin=0; iLin<TAILLE; iLin++)
		for(int iCol=0; iCol<TAILLE; iCol++)
			scanf("%d", &grille[iLin][iCol]);
}

int main(){
	int nbCases;
	scanf("%d", &nbCases);
	for(int iCase = 1; iCase<=nbCases; iCase++){
		int ligne;
		scanf("%d", &ligne);
		lireGrille();
		rempliPoss(ligne-1);
		scanf("%d", &ligne);
		lireGrille();
		int rep = soluce(ligne-1);
		printf("Case #%d: ", iCase);
		if(rep==-1)
			printf("Volunteer cheated!\n"); 
		
		else if(rep==-2)
			printf("Bad magician!\n"); 
		else
			printf("%d\n", rep);
		
	}

}
