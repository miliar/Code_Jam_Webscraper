#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>

using namespace std;

//bool isSqr(double);
unsigned long long strToULLI(string);
bool isPal (unsigned long long);

int main( int argc, char* argv[])
{
	string lwrBndStr, uprBndStr;
	unsigned long long lowerBound, upperBound;
	int nbCase;
	unsigned int nbCount=0;
	unsigned short int rest;

	fstream inputFile("A-small-practice.in", fstream::in);
	fstream outputFile("output.out", fstream::out);

	if( inputFile == NULL)
	{
		cout << "Fichier introuvable"<< endl;
		return -1;
	}
	inputFile >> nbCase;
	for(int i =0; i < nbCase ; i++)
	{
		inputFile >> lwrBndStr >> uprBndStr; 
		lowerBound = ceil(sqrt(strToULLI(lwrBndStr)));	
		upperBound = floor(sqrt(strToULLI(uprBndStr)));
		outputFile << "Case #" << i+1 << ": ";

		for (unsigned long long j = lowerBound ; j <= upperBound ; j++)
		{		
			//cout << j*j << endl;
			if(isPal (j) && isPal(j*j))
			{
				//cout << j*j << endl;
				nbCount++;
			}

		}
		outputFile << nbCount<< endl;
		nbCount = 0;
	}
	
	inputFile.close();
	outputFile.close();

	return 0;
}

bool isSqr(double var)
{
	if(sqrt(var) - ceil(sqrt(var)) == 0)
		return true;
	else
		return false;
}

unsigned long long strToULLI(string str)
{
	unsigned long long result =0;
	for (unsigned long long i = 0 ; i< str.length() ; i ++)
	{
		result *=10;
		result += ((int)(str[i])-48);		
		//cout << (int)(str[i]) -48;
	}
	//cout << endl;
	return result;
}

bool isPal (unsigned long long nb)
{
	unsigned long long res = 0;
	unsigned long long reste;
	unsigned long long quot = nb ;	
	//double tmp = nb;
	
	while(quot != 0)
	{
		res *=10;
		reste = quot%10;
		quot =(quot -reste)/10;
		res += reste;
	}
	if(res == nb)
		return true;
	return false;
}


/*bool isPal (double str)
{
	unsigned long int max = (str.length() % 2 == 0)?str.length():(str.length() -1);
	
	for (unsigned long int i = 0 ; i < max ; i ++)
	{
		if(str[i] != str[str.length()-1-i])
			return false;
	}
	return true;
}*/