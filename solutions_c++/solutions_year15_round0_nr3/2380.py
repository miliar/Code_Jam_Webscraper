#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

enum EQ_ID
{
	EQ_1, EQ_i, EQ_j, EQ_k, EQ_m1, EQ_mi, EQ_mj, EQ_mk
};

EQ_ID operator*(EQ_ID EQ_a, EQ_ID EQ_b)
{
	switch (EQ_a)
	{
	case EQ_1:	return EQ_b;
		break;
	case EQ_i:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_i;	break;
		case EQ_i:	return EQ_m1;	break;
		case EQ_j:	return EQ_k;	break;
		case EQ_k:	return EQ_mj;	break;
		case EQ_m1:	return EQ_mi;	break;
		case EQ_mi:	return EQ_1;	break;
		case EQ_mj:	return EQ_mk;	break;
		case EQ_mk:	return EQ_j;	break;
		}
		break;
	case EQ_j:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_j;	break;
		case EQ_i:	return EQ_mk;	break;
		case EQ_j:	return EQ_m1;	break;
		case EQ_k:	return EQ_i;	break;
		case EQ_m1:	return EQ_mj;	break;
		case EQ_mi:	return EQ_k;	break;
		case EQ_mj:	return EQ_1;	break;
		case EQ_mk:	return EQ_mi;	break;
		}
		break;
	case EQ_k:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_k;	break;
		case EQ_i:	return EQ_j;	break;
		case EQ_j:	return EQ_mi;	break;
		case EQ_k:	return EQ_m1;	break;
		case EQ_m1:	return EQ_mk;	break;
		case EQ_mi:	return EQ_mj;	break;
		case EQ_mj:	return EQ_i;	break;
		case EQ_mk:	return EQ_1;	break;
		}
		break;
	case EQ_m1:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_m1;	break;
		case EQ_i:	return EQ_mi;	break;
		case EQ_j:	return EQ_mj;	break;
		case EQ_k:	return EQ_mk;	break;
		case EQ_m1:	return EQ_1;	break;
		case EQ_mi:	return EQ_i;	break;
		case EQ_mj:	return EQ_j;	break;
		case EQ_mk:	return EQ_k;	break;
		}
		break;
	case EQ_mi:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_mi;	break;
		case EQ_i:	return EQ_1;	break;
		case EQ_j:	return EQ_mk;	break;
		case EQ_k:	return EQ_j;	break;
		case EQ_m1:	return EQ_i;	break;
		case EQ_mi:	return EQ_m1;	break;
		case EQ_mj:	return EQ_k;	break;
		case EQ_mk:	return EQ_mj;	break;
		}
		break;
	case EQ_mj:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_mj;	break;
		case EQ_i:	return EQ_k;	break;
		case EQ_j:	return EQ_1;	break;
		case EQ_k:	return EQ_mi;	break;
		case EQ_m1:	return EQ_j;	break;
		case EQ_mi:	return EQ_mk;	break;
		case EQ_mj:	return EQ_m1;	break;
		case EQ_mk:	return EQ_i;	break;
		}
		break;
	case EQ_mk:
		switch (EQ_b)
		{
		case EQ_1:	return EQ_mk;	break;
		case EQ_i:	return EQ_mj;	break;
		case EQ_j:	return EQ_i;	break;
		case EQ_k:	return EQ_1;	break;
		case EQ_m1:	return EQ_k;	break;
		case EQ_mi:	return EQ_j;	break;
		case EQ_mj:	return EQ_mi;	break;
		case EQ_mk:	return EQ_m1;	break;
		}
		break;
	}
}

EQ_ID charToEq(char charCour)
{
	switch (charCour)
	{
	case 'i':	return EQ_i;	break;
	case 'j':	return EQ_j;	break;
	case 'k':	return EQ_k;	break;
	default:	return EQ_1;	break;
	}
}

int main()
{
	int T(0);
	cin >> T;
	int L;
	int X;
	string input;
	bool trouve;
	int tailleInput;
	int tailleTotale;
	EQ_ID valI;
	EQ_ID valJ;
	EQ_ID valK;
	for (int l = 1; l <= T; l++)
	{
		cin >> L >> X >> input;
		tailleInput = (int)input.size();
		tailleTotale = tailleInput*X;

		if (tailleTotale < 3)
		{
			cout << "Case #" << l << ": NO" << endl;
		}
		else if (tailleTotale == 3)
		{
			if (input == "ijk")
			{
				cout << "Case #" << l << ": YES" << endl;
			}
			else
			{
				cout << "Case #" << l << ": NO" << endl;
			}
		}
		else
		{
			trouve = false;
			//Plus de 3 caractères dans le tableau
			valI = EQ_1;
			for (int x = 0; x < tailleTotale && !trouve; x++)
			{
				valI = valI*charToEq(input[x % tailleInput]);
				if (valI == EQ_i)
				{
					valJ = EQ_1;
					for (int y = x+1; y < tailleTotale && !trouve; y++)
					{
						valJ = valJ*charToEq(input[y % tailleInput]);
						if (valJ == EQ_j)
						{
							valK = EQ_1;
							for (int z = y+1; z < tailleTotale && !trouve; z++)
							{
								valK = valK*charToEq(input[z % tailleInput]);
								if (valK == EQ_k && z == tailleTotale - 1)
								{
									cout << "Case #" << l << ": YES" << endl;
									trouve = true;
								}
							}

						}
					}
				}
			}
			if (!trouve)
			{
				cout << "Case #" << l << ": NO" << endl;
			}

		}


	}
}
