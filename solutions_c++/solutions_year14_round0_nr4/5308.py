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
#include <algorithm>
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
			int tot;
			vector<double> Ela, Ele;
			getline(input,line);
			std::istringstream iss2(line);
			getline(input,line);

			std::istringstream issEla(line);
			getline(input,line);
			std::istringstream issEle(line);
			iss2>>tot;
			Ela.resize(tot);
			Ele.resize(tot);
			double array[10];
			for (int j=0;j<10;j++)
				array[j]=-1;
			for(int j=0;j<tot;j++){
				issEla >> answerAux;
				array[9-j]=answerAux;
			}
			int elements = sizeof(array) / sizeof(array[0]); 
  std::sort(array, array + elements);
  for(int j=0;j<tot;j++){
				Ela[tot-1-j]=array[9-j];
			}
  for (int j=0;j<10;j++)
	  array[j]=-1;
			for(int j=0;j<tot;j++){
				issEle >> answerAux;
				array[9-j]=answerAux;
			}
  elements = sizeof(array) / sizeof(array[0]); 
  std::sort(array, array + elements);
			for(int j=0;j<tot;j++){
				Ele[tot-1-j]=array[9-j];
			}
			int cheat,notCheat;
			int bottonO=0;
			int top0=tot-1;
			cheat=0;
			notCheat=0;
			int topEla,topEle,bottonEla,bottonEle;
			topEla=tot-1;
			topEle=tot-1;
			bottonEla=0;
			bottonEle=0;
			for (int j=0;j<tot;j++){
				if(Ela[tot-1-j]>Ele[top0]){
					notCheat++;
					bottonO++;
				}
				else{
					top0--;
				}
				int naoPerdeu=1;
				for (int k=j;k<tot && cheat==0;k++){
					if(Ela[k]<Ele[k-j])
						naoPerdeu=0;
				}
				if(cheat==0 && naoPerdeu==1)
					cheat=tot-j;
			}
			output<<"Case #"<<i+1<<": "<<cheat<<" "<<notCheat<<'\n';

		}
	}
	output.close();
    return 0;
}
