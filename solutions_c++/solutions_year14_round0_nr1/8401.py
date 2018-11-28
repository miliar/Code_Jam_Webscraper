// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// CodeChef.cpp : Defines the entry point for the console application.
//



#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

char ** splitString(char* str);
int countPossibilities(long unsigned int N, long unsigned int& totalNumberOfCombinations);
void LINA(std::string* line, int count);

struct cardArrangement
{
	std::string row1;
	std::string row2;
	std::string row3;
	std::string row4;
};

int main(int argc, char* argv[])
{
	int N = 11;

	std::ofstream myfile;
	myfile.open ("example.out");
	std::ifstream file(argv[1]);
	
	if ( ! file ) // check if the file loaded fine.
	{
		return -1;
	}
	std::string name;
	std::getline(file,name);
	
	N = atoi(name.c_str());
	std::string* line = NULL;
	int lineCounter = 0;
	int testCases = N;
	while(N > 0)
	{
		std::string firstQ, secondQ;
		cardArrangement arr1, arr2;

		std::getline(file,firstQ);
		std::getline(file,arr1.row1);
		std::getline(file,arr1.row2);
		std::getline(file,arr1.row3);
		std::getline(file,arr1.row4);

		std::getline(file,secondQ);
		std::getline(file,arr2.row1);
		std::getline(file,arr2.row2);
		std::getline(file,arr2.row3);
		std::getline(file,arr2.row4);

		int Q1 = atoi(firstQ.c_str());
		std::string possibleCards1;
		int Q2 = atoi(secondQ.c_str());
		std::string possibleCards2;

		switch(Q1)
		{
			case 1:
				possibleCards1 = arr1.row1;
				break;
			case 2:
				possibleCards1 = arr1.row2;
				break;
			case 3:
				possibleCards1 = arr1.row3;
				break;
			case 4:
				possibleCards1 = arr1.row4;
				break;
		}

		switch(Q2)
		{
			case 1:
				possibleCards2 = arr2.row1;
				break;
			case 2:
				possibleCards2 = arr2.row2;
				break;
			case 3:
				possibleCards2 = arr2.row3;
				break;
			case 4:
				possibleCards2 = arr2.row4;
				break;
		}

		char *cstr1 = new char[possibleCards1.length() + 1];
		strcpy(cstr1, possibleCards1.c_str());

		char *cstr2 = new char[possibleCards2.length() + 1];
		strcpy(cstr2, possibleCards2.c_str());

		char** p1 = splitString(cstr1);
		char** p2 = splitString(cstr2);

		int matches = 0;
		int firstNumbner = -1;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(atoi(p1[i]) ==  atoi(p2[j]))
				{
					matches++;
					if(firstNumbner = -1)
						firstNumbner = atoi(p1[i]);
				}
			}
		}

		char outLine[100];
		if(matches == 0)
			sprintf(outLine,"Case #%d: %s \n", testCases-N+1, "Volunteer cheated!");//Case #3: 
		else if(matches == 1)
			sprintf(outLine,"Case #%d: %d \n", testCases-N+1, firstNumbner);//Case #3: 
		else if(matches > 1)
			sprintf(outLine,"Case #%d: %s \n", testCases-N+1, "Bad magician!");//Case #3: 

		 myfile << outLine;

		N--;
	}

	myfile.close();
	delete[] line;
	return 0;
}
/*
void LINA(std::string* line, int count)
{
	if(count == 0)
		return;

	int smallestIndex = 0;
	int largestIndex = 0;

	int secondSmallestIndex = 0;
	int secondLargestIndex = 0;
	double smallest, largest;
	for(int i = 0; i < count && count > 1; i++)
	{
		char *cstr = new char[line[i].length() + 1];
		strcpy(cstr, line[i].c_str());
		
		char** triangleValues = splitString(cstr);

		triangle current;
		current.x0 = atoi(triangleValues[0]);
		current.y0 = atoi(triangleValues[1]);
		current.x1 = atoi(triangleValues[2]);
		current.y1 = atoi(triangleValues[3]);
		current.x2 = atoi(triangleValues[4]);
		current.y2 = atoi(triangleValues[5]);

		delete triangleValues;
		triangleValues = NULL;

		double a = sqrt(pow((current.x1-current.x0),2.0) + pow((current.y1-current.y0),2.0));
		double b = sqrt(pow((current.x2-current.x1),2.0) + pow((current.y2-current.y1),2.0));
		double c = sqrt(pow((current.x2-current.x0),2.0) + pow((current.y2-current.y0),2.0));
		double p = (a+b+c)/2.00;

		double pp = p*((p-a)*(p-b)*(p-c));
		//double area = sqrt(pp);
		double area = abs((current.x1*current.y0-current.x0*current.y1)+(current.x2*current.y1-current.x1*current.y2)+(current.x0*current.y2-current.x2*current.y0))/2.00;
		printf("%d %1.5f\n", i+1, area);
		if(i == 0)
		{
			smallest = area;
			largest = area;
		}
		else
		{
			if(smallest >= area && area > 0.0)
			{
				secondSmallestIndex = smallestIndex;
				smallestIndex = i;
				smallest = area;
			}
			if(largest <= area && area > 0.0)
			{
				secondLargestIndex = largestIndex;
				largestIndex = i;
				largest = area;
			}
		}
		delete [] cstr;
		cstr = NULL;
	}

	if(smallestIndex == largestIndex)
	{
		//if(secondSmallestIndex > smallestIndex)
			largestIndex = secondLargestIndex;

	}

		printf("%d %d\n", smallestIndex+1, (largestIndex+1));


}
*/
char ** splitString(char* str)
{
	char ** res  = NULL;
	char *  p    = strtok (str, " ");
	int n_spaces = 0, i;



	while (p)
	{
		res = (char **)realloc (res, sizeof (char*) * ++n_spaces);

		if (res == NULL)
			exit (-1);

		res[n_spaces-1] = p;

		p = strtok (NULL, " ");
	}



	res = (char **)realloc(res, sizeof (char*) * (n_spaces+1));
	res[n_spaces] = 0;

	return res;
}
