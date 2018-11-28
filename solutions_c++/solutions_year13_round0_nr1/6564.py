#include <iostream>
#include <fstream>
#include <string>


using namespace std;

//X = 10 O = -10 T=1 . = 0
int grade(char c)
{
	switch (c)
	{
	case '.':
		return 0;		
	case 'O':
		return -10;
	case 'X':
		return 10;
	case 'T':
		return 1;
	case '\n':
		return 42;
	default:
		return -12000;
	}
}
//0 draw 1 x win -1 o win 100 dunno
int winner(int score)
{
	switch (score)
	{
	case 31:
		return 1;
	case 40:
		return 1;
	case -40:
		return -1;
	case -29:
		return -1;
	default:
		return 0;
	}
}


int main(int argc, char* argv)
{

	int tab[16];
	int nbCas;
	int nbPoint =0;
	char c = '.';

	fstream inputFile("A-small-practice.in", fstream::in);
	fstream outputFile("output.out", fstream::out);

	if( inputFile == NULL)
	{
		cout << "Fichier introuvable"<< endl;
		return -1;
	}
	inputFile >> nbCas;
	for (int j=0; j < nbCas; j++)
	{
		cout << "Case #"<<j+1<< ": ";
		outputFile << "Case #"<<j+1<< ": ";
		int currentWinner =0;
		int i =0;
		while (inputFile.good() && i < 16)
		{
			//cout << c ;
			inputFile.get(c);
			if (c =='\n')
				inputFile.get(c);
			if (c =='\n')
				inputFile.get(c);
			tab[i] = grade(c);
			//cout << i << " : " << grade (c) << endl;
			if (c == '.')
				nbPoint ++;
			i++; 
		}
		int sum1 = 0, sum2=0, sum3 = 0, sum4 =0;
		for(int k = 0; k<4 ; k++)
		{
			sum1=tab[4*k]+ tab[4*k+1] + tab[4*k+2] + tab[4*k+3];
			sum2=tab[k]+ tab[4+k] + tab[k+8] + tab[k+12];
			if(winner(sum1) == 1 || winner(sum2) == 1)
			{
				currentWinner = 1;
				break;
			}
			if(winner(sum1) == -1 || winner(sum2) == -1)
			{
				currentWinner = -1;
				break;
			}
		}

		sum3=tab[0]+ tab[5] + tab[10] + tab[15];
		sum4=tab[3]+ tab[6] + tab[9] + tab[12];

		if(winner(sum3) == 1 || winner(sum4) == 1)
		{
			currentWinner = 1;
			//break;
		}
		if(winner(sum3) == -1 || winner(sum4) == -1)
		{
			currentWinner = -1;
			//break;
		}
		if (currentWinner == 1)
		{
			cout << "X won" << endl;
			outputFile << "X won" << endl;
		}
		if (currentWinner == -1)
		{
			cout << "O won" << endl;
			outputFile << "O won" << endl;
		}
		if (currentWinner == 0 && nbPoint > 0)
		{
			cout << "Game has not completed" << endl;
			outputFile << "Game has not completed" << endl;
		}
		if (currentWinner == 0 && nbPoint == 0 )
		{
			cout << "Draw" << endl;
			outputFile << "Draw" << endl;
		}

		//delete tab;
			nbPoint = 0;
	}


	inputFile.close();
	outputFile.close();
	//cout << sizeof("test");
	//system("pause");
	return 1;
}
