#include <cstdio>
#include <set>
using namespace std;

struct fichier {
	int poids, id;
	bool operator<(const fichier &a) const {
		return (poids < a.poids) || (poids == a.poids && id < a.id);
	}
};

int main(void) {
	int nbTests;
	scanf("%d", &nbTests);
	for (int test = 1; test <= nbTests; test++) {
		int nbFichiers, tailleMax;
		set<fichier> restants;
		scanf("%d%d", &nbFichiers, &tailleMax);
		for (int i = 0; i < nbFichiers; i++) {
			fichier nouv;
			scanf("%d", &nouv.poids);
			nouv.id = i;
			restants.insert(nouv);
		}
		int total = 0;
		while (!restants.empty()) {
			set<fichier>::iterator fin = restants.end();
			fin--;
			fichier cour = *fin;
			restants.erase(fin);
			total++;
			if (restants.empty())
				break;
			fichier recherche;
			recherche.poids = tailleMax-cour.poids;
			recherche.id = -1;
			set<fichier>::iterator avec = restants.lower_bound(recherche);
			if (avec == restants.begin()) {
				if (cour.poids + (*avec).poids <= tailleMax) {
					restants.erase(avec);
				}
			} else {
				avec--;
				if (cour.poids + (*avec).poids <= tailleMax) {
					restants.erase(avec);
				}
			}
		}
		printf("Case #%d: %d\n", test, total);
	}
	return 0;
}
