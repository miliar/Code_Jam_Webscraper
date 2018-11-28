// JakesProject.cpp : main project file.
#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include "vector"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <time.h>
using namespace std;
;

int main(array<System::String ^> ^args)
{
		ifstream input;
	input.open("input.txt");
	string line;
	double cases;
	
	ofstream output;
	output.open("output.txt");
	
	if (input.is_open())
	{
		getline(input,line);
		std::istringstream iss(line);
		iss >> cases;
		for (int i=0;i<cases;i++){
			double answerAux;
			vector<double> vetor;
			vetor.resize(3);
			getline(input,line);
			std::istringstream iss2(line);
			for(int j=0;j<3;j++){
				iss2 >> answerAux;
				vetor[j]=answerAux;
			}
			int BestFound=0;
			int now=0;
			double lowestTime=vetor[2]/2;
			while (BestFound==0){
				now=now+1;
				double sum=0;
				for(int k=0;k<now;k++){
					sum=sum+(vetor[0]/(2+vetor[1]*k));
				}
				sum=sum+vetor[2]/(2+vetor[1]*now);
				if (sum>lowestTime)
					BestFound=1;
				else
					lowestTime=sum;
			}
			output.precision(0);
			output<<"Case #"<<i+1<<": ";
			output.precision(12);
			output << lowestTime << '\n';;

		}
	}
	output.close();
    return 0;
}
