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
			int answer,answerAux;
			vector <vector<int> > vetor;
			vetor.resize(2);
			vetor[0].resize(4);
			vetor[1].resize(4);
			getline(input,line);
			std::istringstream iss2(line);

			iss2 >> answer;
			for (int j=0;j<answer;j++){
				getline(input,line);
			}
			std::istringstream iss3(line);
			for(int j=0;j<4;j++){
				iss3 >> answerAux;
				vetor[0][j]=answerAux;
			}
			for (int j=answer;j<4;j++){
				getline(input,line);
			}
			getline(input,line);
			std::istringstream iss5(line);
			iss5 >> answerAux;
			for (int j=0;j<answerAux;j++){
				getline(input,line);
			}
			std::istringstream iss4(line);
			int resposta;
			for(int j=0;j<4;j++){
				iss4 >> answer;
				for (int k=0;k<4;k++){
					if (answer==vetor[0][k]){
						vetor[1][k]=1;
						resposta=vetor[0][k];
					}
				}
			}
			for (int j=answerAux;j<4;j++){
				getline(input,line);
			}
			output<<"Case #"<<i+1<<": ";
			if (vetor[1][0]+vetor[1][1]+vetor[1][2]+vetor[1][3]>1)
				output<<"Bad magician!\n";
			else{
				if (vetor[1][0]+vetor[1][1]+vetor[1][2]+vetor[1][3]<1)
					output<<"Volunteer cheated!\n";
				else{
					output<<resposta<<"\n";
				}
			}

		}
	}
	output.close();
    return 0;
}
