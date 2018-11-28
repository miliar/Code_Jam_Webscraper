#include <cstdio>
#include <algorithm>
using namespace std;
int game[100][100];

int maxparcolonne[100];
int maxparligne[100];
int main()
{
	int n;
	scanf("%d", &n);
	for(int g = 0; g < n; g++)
	{
		int hauteur, largeur;
		scanf("%d%d", &hauteur,&largeur);
		fill(maxparcolonne, maxparcolonne + 100, 0);
		fill(maxparligne, maxparligne + 100, 0);
		for(int l = 0; l < hauteur; l++)
		{
			for(int c = 0; c < largeur; c++)
			{
				scanf("%d", &game[l][c]);
				maxparcolonne[c] = max(maxparcolonne[c], game[l][c]);
				maxparligne[l] = max(maxparligne[l], game[l][c]);
			}
		}
		bool resultat = true;
		for(int l = 0; l < hauteur; l++)
		{
			for(int c = 0; c < largeur; c++)
			{
				if(game[l][c] != min(maxparligne[l], maxparcolonne[c]))
					resultat = false;
			}
		}
		printf("Case #%d: ", g+1);
		if(resultat)
			printf("YES");
		else printf("NO");
		printf("\n");
	}
	return 0;
}
