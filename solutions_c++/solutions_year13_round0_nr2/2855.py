#include <iostream>
#include <string>
#include <stack>
#include <cstdlib>

using namespace std;

int TEST_CASES;

int lawn[100][100];
int valori[100][100];

		int N,M;

void azzera_valori()
{
	for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				valori[i][j] = 0;
}

int verifica_valori()
{
	for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (valori[i][j] == 0) return 0;
	return 1;
}


void stampa()
{
	for (int i = 0; i < N; i++)
	{
			for (int j = 0; j < M; j++)
				cout << lawn[i][j] << " ";
			cout << endl;
	}
	for (int i = 0; i < N; i++)
	{
			for (int j = 0; j < M; j++)
				cout << valori[i][j] << " ";
			cout << endl;
	}
}
				
int main()
{
    cin >> TEST_CASES;
    for (int c = 0; c < TEST_CASES; c++)
    {
		azzera_valori();
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				cin >> lawn[i][j];
		for (int i = 0; i < N; i++)
		{
			int max = lawn[i][0];
			for (int j = 0; j < M; j++)
				if (lawn[i][j] > max) max = lawn[i][j];
			for (int j = 0; j < M; j++)
				if (lawn[i][j] == max) valori[i][j] = 1;
		}
		for (int i = 0; i < M; i++)
		{
			int max = lawn[0][i];
			for (int j = 0; j < N; j++)
				if (lawn[j][i] > max) max = lawn[j][i];
			for (int j = 0; j < N; j++)
				if (lawn[j][i] == max) valori[j][i] = 1;
		}
		int ris = verifica_valori();
		//stampa();
		if (ris == 0)
			cout << "Case #" << c+1 << ": NO" << endl ;
		if (ris == 1)
			cout << "Case #" << c+1 << ": YES" << endl ;
    }
    return 0;
}
