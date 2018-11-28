#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <cmath>
#include <map>
#include <queue>
#include <fstream>

using namespace std;


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("output.txt");

	int T, i, k;
	string cake;
	fin >> T;

	for (int casen = 1; casen <= T; casen++){
		fin >> cake;
		for (int j = 0;; j++){
			for (i = cake.length() - 1; i >= 0; i--){
				if (cake[i] == '-')
					break;
			}

			if (i == -1){
				fout << "Case #" << casen << ": " << j << endl;
				break;
			}

			string temp = "";
			int check = 0;
			for (k = 0; k < cake.length(); k++){
				if (check <= 1 && cake[k] == '+'){
					temp += '-';
					check = 1;
				}
				else{
					if (check <= 1)
						check += 2;

					temp += cake[k];
				}
			}

			if (check == 3)
				j++;

			cake = temp;
			
			temp = "";
			for (k = i; k >= 0; k--){
				if (cake[k] == '+')
					temp += '-';
				else
					temp += '+';
			}
			for (k = i + 1; k < cake.length(); k++)
				temp += cake[k];

			cake = temp;
		}
	}
}