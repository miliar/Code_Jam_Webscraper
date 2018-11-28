/*
 * problemA.cpp
 *
 *  Created on: Apr 11, 2014
 *      Author: filipebraida
 */
#include<iostream>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

const int MAX_JOGOS = 100;
const int MAX_CLICKS = 100;

using namespace std;

void roda_jogo(char **, int, int, int, int);
bool verifica_vitoria_click_jogo(char **, int, int, int, int);
void generateJogo(int, int, int);
void coloca_minas_aleatorias(char **, int, int, int);
void coloca_minas_espiral(char **, int, int, int);
void coloca_minas(char **, int, int, int, int *);
bool verifica_clicks_jogo(char **, int, int);


/* Prints out a combination like {1, 2} */
void printc(int comb[], int k) {
	printf("{");
	int i;
	for (i = 0; i < k; ++i)
		printf("%d, ", comb[i] + 1);
	printf("\b\b}\n");
}

/*
	next_comb(int comb[], int k, int n)
		Generates the next combination of n elements as k after comb

	comb => the previous combination ( use (0, 1, 2, ..., k) for first)
	k => the size of the subsets to generate
	n => the size of the original set

	Returns: 1 if a valid combination was found
		0, otherwise
*/
int next_comb(int comb[], int k, int n) {
	int i = k - 1;
	++comb[i];
	while ((i >= 0) && (comb[i] >= n - k + 1 + i)) {
		--i;
		++comb[i];
	}

	if (comb[1] > n - k) /* Combination (n-k, n-k+1, ..., n) reached */
		return 0; /* No more combinations can be generated */

	/* comb now looks like (..., x, n, n, n, ..., n).
	Turn it into (..., x, x + 1, x + 2, ...) */
	for (i = i + 1; i < k; ++i)
		comb[i] = comb[i - 1] + 1;

	return 1;
}

int* combinate(int n, int k) {
	int comb[16]; /* comb[i] is the index of the i-th element in the
			combination */

	/* Setup comb for the initial combination */
	int i;
	for (i = 0; i < k; ++i)
		comb[i] = i;

	/* Print the first combination */
	printc(comb, k);

	/* Generate and print all the other combinations */
	while (next_comb(comb, k, n))
		printc(comb, k);

	return comb;
}

char** create2dArray(char rows, int cols) {
	char** array = new char*[rows];
	for (int row=0; row<rows; row++) {
		array[row] = new char[cols];
	}
	return array;
}

void loadDefault(char **ar, int rows, int cols) {
	for (int row=0; row<rows; row++) {
		for (int col=0; col<cols; col++) {
			ar[row][col] = '.';
		}
	}
}

char** duplicate(char **ar, char rows, int cols) {
	char **ar2 = create2dArray(rows, cols);

	for (int row=0; row<rows; row++) {
		for (int col=0; col<cols; col++) {
			ar2[row][col] = ar[row][col];
		}
	}

	return ar2;
}

void print(char **ar, int rows, int cols) {
	for (int row=0; row<rows; row++) {
		for (int col=0; col<cols; col++) {
			cout << ar[row][col];
		}
		cout << endl;
	}
}

void delete2dArray(char **ar, int rows, int cols) {
	for (int row=0; row<rows; row++) {
		delete [] ar[row];
	}
	delete [] ar;
}

int main(void)
{
	srand (time(NULL));

	int R, C, M;

	int test_cases;

	cin >> test_cases;

	for(int n = 0; n < test_cases; n++)
	{
		cin >> R;
		cin >> C;
		cin >> M;
		cin.get();

		cout << "Case #" << n + 1 << ": " << endl;

		generateJogo(R, C, M);
	}

	return 0;
}

void generateJogo(int R, int C, int M)
{
	char **jogo = create2dArray(R, C);
	loadDefault(jogo, R, C);

	int n = R * C;
	int k = M;

	int comb[M];

	/* Setup comb for the initial combination */
	int i;
	for (i = 0; i < k; ++i)
		comb[i] = i;

	int tentativas = 10000;

	/* Generate and print all the other combinations */
	do
	{
		char **jogo_minas = duplicate(jogo, R, C);

		coloca_minas(jogo_minas, R, C, M, comb);

		//print(jogo_minas, R, C);
		//printc(comb, M);

		if(verifica_clicks_jogo(jogo_minas, R, C))
		{
			print(jogo_minas, R, C);
			delete2dArray(jogo, R, C);
			delete2dArray(jogo_minas, R, C);
			return;
		}

		if(tentativas++ > 25000) break;

		delete2dArray(jogo_minas, R, C);

	} while (next_comb(comb, k, n));

	cout << "Impossible" << endl;
	delete2dArray(jogo, R, C);

	return;
}

void coloca_minas(char **jogo, int R, int C, int M, int *comb)
{
	for(int i = 0; i < M; i++)
	{
		int y = (int)((comb[i]) / R);
		int x = comb[i] % R;

		jogo[x][y] = '*';
	}
}

void coloca_minas_espiral(char **jogo, int R, int C, int M)
{
	int rs=0, cs=0;     // RowStart and Column Start
	int re=R-1, ce=C-1;  // RowEnd & columnEnd

	int m = 0;

	while(rs<=re && cs<=ce)
	{
		int i=rs, j=cs;

		for(j=cs; j<=ce; j++)
		{
			jogo[i][j] = '*';
			m = m + 1;

			if(m >= M)
				return;
		}

		for(i=rs+1, j--; i<=re; i++)
		{
			jogo[i][j] = '*';
			m = m + 1;

			if(m >= M)
				return;

		}

		for(j=ce-1, i--; j>=cs; j--)
		{
			jogo[i][j] = '*';
			m = m + 1;

			if(m >= M)
				return;
		}

		for(i=re-1, j++; i>=rs+1; i--)
		{
			jogo[i][j] = '*';
			m = m + 1;

			if(m >= M)
				return;
		}

		rs++; cs++; re--; ce--;
	}
}


void coloca_minas_aleatorias(char **jogo, int R, int C, int M)
{
	for(int i=0; i < M; i++)
	{
		int x = rand() % R;
		int y = rand() % C;

		if(jogo[x][y] == '.')
		{
			jogo[x][y] = '*';
		}
		else
		{
			i = i - 1;
			continue;
		}
	}
}

bool verifica_clicks_jogo(char **jogo, int R, int C)
{
	for(int gen_clicks = 0; gen_clicks < R * C  * MAX_CLICKS; gen_clicks++)
	{
		int x = rand() % R;
		int y = rand() % C;

		if(gen_clicks == 0)
		{
			x = R / 2;
			y = R / 2;
		}

		if(verifica_vitoria_click_jogo(jogo, R, C, x, y))
		{
			jogo[x][y] = 'c';

			return true;
		}
	}

	return false;
}

bool verifica_vitoria_click_jogo(char **jogo, int R, int C, int x, int y)
{
	char **jogo_rodado = duplicate(jogo, R, C);

	roda_jogo(jogo_rodado, R, C, x, y);

	bool achei = false;

	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			if(jogo_rodado[i][j] == '.')
				achei = true;
		}
	}

    delete2dArray(jogo_rodado, R, C);

    if(achei)
    	return false;

	return true;
}

void roda_jogo(char **jogo, int R, int C, int x, int y)
{
	if(x < 0 || y < 0 || x >= R || y >= C)
		return;

	if(jogo[x][y] != '.')
		return;

	int bombas = 0;
	if(x-1 >= 0 && y-1 >= 0 	&& jogo[x-1][y-1] == '*')	bombas += 1;
	if(x-1 >= 0 				&& jogo[x-1][y] == '*')		bombas += 1;
	if(y-1 >= 0 				&& jogo[x][y-1] == '*')		bombas += 1;
	if(x+1 < R && y+1 < C 		&& jogo[x+1][y+1] == '*')	bombas += 1;
	if(y+1 < C 					&& jogo[x][y+1] == '*')		bombas += 1;
	if(x+1 < R 					&& jogo[x+1][y] == '*')		bombas += 1;
	if(x-1 >= 0 && y+1 < C 		&& jogo[x-1][y+1] == '*') 	bombas += 1;
	if(x+1 < R && y-1 >= 0 		&& jogo[x+1][y-1] == '*') 	bombas += 1;

	jogo[x][y] = '0' + bombas;

	if(bombas == 0)
	{
		roda_jogo(jogo, R, C, x-1, y-1);
		roda_jogo(jogo, R, C, x, y-1);
		roda_jogo(jogo, R, C, x, y+1);
		roda_jogo(jogo, R, C, x-1, y);
		roda_jogo(jogo, R, C, x+1, y);
		roda_jogo(jogo, R, C, x-1, y+1);
		roda_jogo(jogo, R, C, x+1, y-1);
		roda_jogo(jogo, R, C, x+1, y+1);
	}
}
