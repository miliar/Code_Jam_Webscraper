// GoogleJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include <string>
#include "iostream"


using namespace std;

int digitCount(int number , bool * Seen) {
	
	int count = 0;
	for (int i = 0; i < 10; i++)
	{
		if (Seen[i] == true)
			count++;
	}
	while (number != 0) {
	
		int digit = number % 10;
		if (Seen[digit] == false) {
		
			++count;
			Seen[digit] = true;
		}
		
		number /= 10;
	}

	return count;
}


int count_sheep(int num,int counter)
{
	bool digitSeen[10]  = { 0 };
	int out = digitCount(num, digitSeen);
	int fact = 2;
	bool INSOMNIA = 0;
	while (out < 10)
	{

		//num = num*fact;
		out = digitCount(num*fact, digitSeen);
		fact++;
	
		if (fact > 100)
		{
			INSOMNIA = 1;
			break;
		}
	}
	if (INSOMNIA)
		return 0;
	else
		return num*(fact-1);
}

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream input("c:/input.txt");
	ofstream output("Output.txt");
	string count;
	getline(input, count);
	int Cases = stoi(count);
	int sheep;
	for (int i = 0; i < Cases; i++)
	{
		getline(input, count);
		sheep = count_sheep(stoi(count), 0);
		output << "Case #" <<(i + 1) <<": ";
		

		if (sheep == 0)
			output << "INSOMNIA" << endl;
		else
			output << sheep << endl;

	}



	

	return 0;
}

