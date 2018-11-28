#include "stdafx.h"


// codejam.cpp : 定义控制台应用程序的入口点。
//



#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>
#include<vector>
#include<stack>
#include<queue>

#define INPUTFILE "A-small-attempt0.in"
#define OUTPUTFILE "result.out"


using namespace std;

//#pragma warning(disable:4996)




int main()
{
	fstream infile(INPUTFILE, ios::in);
	fstream outfile(OUTPUTFILE, ios::out);
	int caseN, count;
	infile >> caseN;
	count = 1;
	//int A, B, K;
	int N,T,i,j,index;
	char data[150][150];
	char pattern[150];
	char temp[150];
	int number[150][150],sum[150];
	char last;
	while (count <= caseN){
		infile >> T;
		for (i = 0; i < T; i++){
			infile >> data[i];
		}
		memset(number, 0, sizeof(number));
		memset(sum, 0, sizeof(sum));
		bool bok = true;
		j = 0;
		index = 0;
		last = '\0';
		while (data[0][j] != '\0'){
			if (data[0][j] != last){
				pattern[index] = data[0][j];
				number[0][index] = 1;
				index++;
				last = data[0][j];
			}
			else
				number[0][index - 1]++;
			j++;
		}
		pattern[index] = '\0';
		for (i = 1; i < T; i++){
			j = 0;
			index = 0;
			last = '\0';
			while (data[i][j] != '\0'){
				if (data[i][j] != last){
					temp[index] = data[i][j];
					number[i][index] = 1;
					index++;
					last = data[i][j];
				}
				else
					number[i][index - 1]++;
				j++;
			}
			temp[index] = '\0';
			if (strcmp(temp, pattern) != 0){
				bok = false;
				break;
			}
		}
		if (!bok){
			outfile << "Case #" << count++ << ": Fegla Won\n";
			continue;
		}
		int answer = 0;
		for (i = 0; pattern[i]!='\0'; i++){
			for (j = 0; j < T; j++)
				sum[i] += number[j][i];
		}
		int one, two,avg;
		for (i = 0; pattern[i] != '\0'; i++){
			one = two = 0;
			avg = sum[i] / T;
			for (j = 0; j < T; j++){
				one += abs(number[j][i] - avg);
				two += abs(number[j][i] - avg - 1);
			}
			answer += (one < two ? one : two);
		}
	
		outfile << "Case #" << count++ << ": " <<answer<< endl;
	}

	infile.close();
	outfile.close();
	return 0;
}

