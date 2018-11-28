// GCJ_2016_QR_A.cpp : Defines the entry point for the console application.
//




#include "stdafx.h"

#include <iostream>
#include <vector>


using namespace std;

bool arr[10];

void div(int value)
{
	while (value)
	{
		int n = value %10;
		value = value / 10;

		arr[n] = true;
	}
}


int main()
{

	//FILE * file = fopen("input.txt", "r");
	//FILE * file = fopen("B-large-practice.in", "r");
	FILE * file = fopen("A-large.in", "r");
	FILE * resfile = fopen("result.txt", "w");


	if (!file)
	{
		cout << "open  Error";
	}


	int TestCount = 0;
	fscanf(file, "%i", &TestCount);



	for (int TestNumber = 1; TestNumber <= TestCount; ++TestNumber)
	{

		cout << "Test # " << TestNumber << endl;

		int N = 0;

		fscanf(file, "%i", &N);
		
		if (N == 0 )
		{
			
			fprintf(resfile, "Case #%i: INSOMNIA\n", TestNumber);
			continue;
		}
		
	

		for (int i = 0;i < 10;++i)
			arr[i] = false;
		int k = 1;
		int res = 0;
		while (N)
		{
			res = N * k;
		
			div(res);
			int i = 0;
			for (i = 0;i < 10;++i)
				if (!arr[i])
					break;

			if (i == 10)
				break;

			++k;
			
		}

	




		fprintf(resfile, "Case #%i: %i\n", TestNumber, res);




	}//


	fclose(file);
	fclose(resfile);


	system("PAUSE");
	return 0;
}

