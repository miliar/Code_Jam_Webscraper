// codejam.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"

#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>

#define INPUTFILE "D-large.in"
#define OUTPUTFILE "result.out"


using namespace std;

//#pragma warning(disable:4996)

int cmp(const void *a, const void *b)
{
	return *(double *)a > *(double *)b ? 1 : -1;
}


int main()
{
	fstream infile(INPUTFILE,ios::in);
	fstream outfile(OUTPUTFILE,ios::out);
	double weightA[1001], weightB[1001];
	int caseN, count, N, i;
	int leftA, rightA, leftB, rightB;
	infile >> caseN;
	count = 1;
	int war,deWar;
	while (count<=caseN)
	{
		infile >> N;
		for (i = 1; i <= N; i++)
			infile >> weightA[i];
		for (i = 1; i <= N; i++)
			infile >> weightB[i];
		qsort(weightA + 1, N, sizeof(double),cmp);
		qsort(weightB + 1, N, sizeof(double),cmp);
		//war;
		rightA = rightB = N;
		war = 0;
		while (rightA>=1){
			if (weightA[rightA] > weightB[rightB]){
				--rightA;
				war++;
			}
			else{
				--rightA;
				--rightB;
			}
		}
		//deWar
		leftA = leftB = 1; rightA = rightB = N;
		deWar = 0;
		while (leftA <= N){
			if (weightA[leftA] < weightB[leftB]){
				++leftA;
				--rightB;
			}
			else{
				++leftA;
				++leftB;
				deWar++;
			}
		}
		outfile << "Case #" << count++ << ": " << deWar << " " << war << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

