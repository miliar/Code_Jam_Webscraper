#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <fstream>
#include <list>
using namespace std;

#define M_PI 3.14159265358979323846

const int maxn = 100 + 5;
const int maxw = 999999;
long long N;
string words[maxn];
long long Result;
int erg[maxn][maxw];
int d[maxw]; // durchschnitt von erg

string sw(int j){	
	int s = 0;
	string word = words[j];
	while (true){
		bool c = false;
		for (int i = 0; i < word.length() - 1; i++)
		{
			if (word[i] == word[i + 1]) {
				c = true;
				string old = word;
				word = word.substr(0, word.length() - 1);
				int oldK = 0;
				for (int k = 0; k < old.length(); k++){
					if (k == i) {
						continue;
					}
					word[oldK] = old[k];
					oldK++;
				}
			}
		}
		if (c == false || word.length() == 1)
			return word;
		if (s == 10000)
			return "";
		s++;
	}
}

void erweitern(string shortest, int j){
	string word = words[j];
	for (int i = 0; i < shortest.length(); i++)
	{
		while (shortest[i] != word[i]){
			erg[j][i-1]++;
			word = word.substr(0, i) + word.substr(i + 1, word.length() - (i + 1)); 
		}
	}
	int x = shortest.length() - 1;
	while (shortest.length() < word.length()){
		erg[j][x] = erg[j][x] + 1;
		word = word.substr(0, x) + word.substr(x + 1, word.length() - (x + 1));
	}
}


int solve2(){
	bool test = true;
	string shortest = "";
	for (int j = 0; j < N; j++){
		string word = sw(j);
		if (shortest == "") shortest = word;
		else if (shortest != word) {
			test = false;
			break;
		}
	}
	
	if (test == false) return -1;
	if (shortest == "") {
		printf("mist");
		return 0;
	}

	for (int i = 0; i < N; i++){
		for (int j = 0; j < shortest.length(); j++) {
			erg[i][j] = 0;
			if (i == 0)
				d[j] = 0;
		}		
	}

	for (int i = 0; i < N; i++)
	{
		erweitern(shortest, i);
	}

	int v = 0;
	for (int i = 0; i < shortest.length(); i++)
	{ 
		for (int j = 0; j < N; j++){
			d[i] += erg[j][i];
		}
		d[i] /= N;
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < shortest.length(); j++){
			v += abs(d[j] - erg[i][j]);
		}
	}


	return v;
}

int main(int argc, char* argv[])
{
	//input variables
	int numberOfTestCases;

	ifstream myfile;
	ofstream outputFile;
	string line;
	myfile.open("input.in");
	outputFile.open("output.out");

	if (myfile.is_open()){
		myfile >> numberOfTestCases;
		getline(myfile, line);

		for (int q = 0; q < numberOfTestCases; q++){
			cout << q << "\n";

			//input
			myfile >> N;

			getline(myfile, line);
			for (int k = 0; k < N; k++){
				getline(myfile, line);				
				words[k] = line;
			}

			//solve problem			
			Result = solve2();

			

			//output			
			switch (Result)
			{
			case -1: outputFile << "Case #" << q + 1 << ": Fegla Won";
				break;
			default: outputFile << "Case #" << q+ 1 << ": " << Result;
				break;
			}

			if (q + 1 != numberOfTestCases)
				outputFile << "\n";
		};
		myfile.close();
		outputFile.close();
	}
	else {
		cout << "unable to open file";
	}
	string name;

	cin >> name;
	return 0;
}

