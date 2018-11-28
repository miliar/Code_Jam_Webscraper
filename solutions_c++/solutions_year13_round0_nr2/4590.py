#include <cstdio>

const int TAILLE = 100, HAUTEUR = 100;

int vrai[TAILLE][TAILLE];
int cour[TAILLE][TAILLE];
bool estCoupable[2][TAILLE];

void couper(bool estCol, int pos, int taille, int nb) {
	for (int i = 0; i < nb; i++) {
		if (estCol)
			cour[i][pos] = taille;
		else
			cour[pos][i] = taille;
	}
}

void afficher(int l, int c) {
	for (int i = 0; i < l; i++) {
		for (int j = 0; j < c; j++)
			printf("%d ", cour[i][j]);
		printf("\n");
	}
	printf("\n");
}

int main(void) {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int nbLin, nbCol;
		bool ok = true;
		scanf("%d%d", &nbLin, &nbCol);
		for (int iLin = 0; iLin < nbLin; iLin++)
			for (int iCol = 0; iCol < nbCol; iCol++) {
				scanf("%d", &vrai[iLin][iCol]);
				cour[iLin][iCol] = HAUTEUR;
			}
		for (int hautMax = HAUTEUR; hautMax >= 1; hautMax--) {
			for (int i = 0; i < TAILLE; i++)
				estCoupable[0][i] = estCoupable[1][i] = true;
			for (int iLin = 0; iLin < nbLin; iLin++)
				for (int iCol = 0; iCol < nbCol; iCol++)
					if (vrai[iLin][iCol] > hautMax)
						estCoupable[0][iLin] = estCoupable[1][iCol] = false;
			for (int iLin = 0; iLin < nbLin; iLin++)
				if (estCoupable[0][iLin]) {
//					printf("On coupe la ligne %d\n", iLin);
					couper(0, iLin, hautMax, nbCol);
				}
			for (int iCol = 0; iCol < nbCol; iCol++)
				if (estCoupable[1][iCol]) {
//					printf("On coupe la colonne %d\n", iCol);
					couper(1, iCol, hautMax, nbLin);
				}
//			afficher(nbLin, nbCol);
		}
		for (int iLin = 0; iLin < nbLin; iLin++)
			for (int iCol = 0; iCol < nbCol; iCol++)
				if (vrai[iLin][iCol] != cour[iLin][iCol])
					ok = false;
		printf("Case #%d: %s\n", test, ok?"YES":"NO");
	}
	return 0;
}
