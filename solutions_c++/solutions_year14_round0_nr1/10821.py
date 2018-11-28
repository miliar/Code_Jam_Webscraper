#include <iostream>
#include <vector>

using namespace std;

void lerGrade(int matriz[4][4]);

int numberOfEqualCards(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4]);

bool isBadMagician(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4]);
bool isVolunteerCheated(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4]);
int equalCards(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4]);

int main()
{
	int numCasosTeste, linhaUm, linhaDois, cartaIgual;

	cin >> numCasosTeste;

	for(int casoTeste = 1; casoTeste <= numCasosTeste; casoTeste++)
	{
		int gradeUm[4][4];
		int gradeDois[4][4];

		cin >> linhaUm;
		linhaUm--;
		lerGrade(gradeUm);

		cin >> linhaDois;
		linhaDois--;
		lerGrade(gradeDois);

		if(isBadMagician(linhaUm, gradeUm, linhaDois, gradeDois))
		{
			cout << "Case #" << casoTeste << ": Bad magician!" << endl;
			continue;
		}

		if(isVolunteerCheated(linhaUm, gradeUm, linhaDois, gradeDois))
		{
			cout << "Case #" << casoTeste << ": Volunteer cheated!" << endl;
			continue;
		}

		cartaIgual = equalCards(linhaUm, gradeUm, linhaDois, gradeDois);
		cout << "Case #" << casoTeste << ": " << cartaIgual << endl;
	}

	return 0;
}

void lerGrade(int matriz[4][4])
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			cin >> matriz[i][j];
		}
	}
}

int numberOfEqualCards(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4])
{
	int cartasIguais;

	cartasIguais = 0;

	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(gradeUm[linhaUm][i] == gradeDois[linhaDois][j])
			{
				cartasIguais++;
			}
		}
	}

	return cartasIguais;
}

bool isBadMagician(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4])
{
	int cartasIguais;

	cartasIguais = numberOfEqualCards(linhaUm, gradeUm, linhaDois, gradeDois);

	return cartasIguais > 1;
}

bool isVolunteerCheated(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4])
{
	int cartasIguais;

	cartasIguais = numberOfEqualCards(linhaUm, gradeUm, linhaDois, gradeDois);

	return cartasIguais == 0;
}

int equalCards(int linhaUm, int gradeUm[4][4], int linhaDois, int gradeDois[4][4])
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(gradeUm[linhaUm][i] == gradeDois[linhaDois][j])
			{
				return gradeUm[linhaUm][i];
			}
		}
	}

	return -1;
}