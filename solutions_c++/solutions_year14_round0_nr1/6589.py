#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <fstream>

using namespace std;

/* PROBLEMA 1 


Problem

Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!

The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?

You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.

Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).
Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input. Once you have solved the Small input, you have finished solving this problem.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.
Limits

1 ≤ T ≤ 100.
1 ≤ both answers ≤ 4.
Each number from 1 to 16 will appear exactly once in each arrangement.
Sample

Input
  	
Output
 

3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

	

Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!



*/

FILE *escribir = fopen("D:\\output.txt", "w");

int nroCasos;
int respuestas[2];

const int NUMERO_CARTAS = 16;
int cartas[NUMERO_CARTAS*2];

int intersectar()
{
	int loteuno[4];

	for (int i = 0; i < 4; i++)
	{
		loteuno[i] = cartas[respuestas[0]*4 - 4 + i];
	}

	int lotedos[4];

	for (int i = 0; i < 4; i++)
	{
		lotedos[i] = cartas[respuestas[1]*4 - 4 + i + 16];
	}

	/*
	Reglas:
	Si la interseccion es 1, se devuelve el numero
	Si la interseccion es > 1, se devuelve -1
	Si no hay interseccion, se devuelve cero
	*/

	int cantidadIguales = 0; // Numero de repeticiones entre los lotes
	int interseccion = 0; // Ultima carta repetida en los lotes
	printf("\n-------------------------");
	for (int i = 0; i < 4; i++)
	{
		for (int k = 0; k < 4; k++)
		{
			printf("%d - %d\n", loteuno[i], lotedos[k]);
			if (loteuno[i] == lotedos[k])
			{
				cantidadIguales++;
				interseccion = loteuno[i];
			}
		}
	}

	if (cantidadIguales == 1)
		return interseccion;
	else if (cantidadIguales > 1)
		return -1;
	else
		return 0;
}

void problemaUno()
{
	FILE *archivo = fopen("D:\\A-small-attempt0.in", "r");
	
	if (archivo != 0)
	{
		fscanf(archivo, "%d", &nroCasos);
		
		for (int caso = 0; caso < nroCasos; caso++)
		{
			int offset = 0;
			for (int k = 0; k < 2; k++)
			{
				fscanf(archivo, "%d", &respuestas[k]);

				if (k > 0)
					offset = 16;

				for (int i = 0; i < NUMERO_CARTAS; i++)
				{
					fscanf(archivo, "%d", &cartas[i+offset]);
					//fscanf(archivo, "%c", NULL);
				}
			}

			/* Hacer intercepcion */
			int resp = intersectar();
			if (resp == 0)
			{
				fprintf(escribir, "Case #%d: Volunteer cheated!\n", (caso+1));				
			}
			else if (resp == -1)
			{
				fprintf(escribir, "Case #%d: Bad magician!\n", (caso+1));				
			}
			else
			{
				fprintf(escribir, "Case #%d: %d\n", (caso+1), resp);				
			}
		}
	}

	fclose(archivo);
}


void main()
{
	problemaUno();
	fclose(escribir);
	system("pause");
}