#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("result.txt");

	int times;

	fin >> times;

	for (int i = 0; i < times; i++){
		int N;
		fin >> N;
		vector<double> naomi_block;
		vector<double> ken_block;

		for (int j = 0; j < N; j++){
			double a;
			fin >> a;
			naomi_block.push_back(a);
		}
		for (int j = 0; j < N; j++){
			double a;
			fin >> a;
			ken_block.push_back(a);
		}

		sort(naomi_block.begin(), naomi_block.end());
		sort(ken_block.begin(), ken_block.end());
		vector<double> naomi_1 = naomi_block;
		vector<double> ken_1 = ken_block;
		/*
		for (int j = 0; j < N; j++){
			cout << naomi_block[j] << " ";
		}
		cout << endl;

		for (int j = 0; j < N; j++){
			cout << ken_block[j] << " ";
		}
		cout << endl;*/

		int wins = 0;
		for (int j = 0; j < N; j++){
			bool is_first = true;
			for (int k = 0; k < ken_block.size(); k++){
				if (is_first && ken_block[k] > naomi_block[j]){
					is_first = false;
					for (int l = k; l < ken_block.size() - 1; l++){
						ken_block[l] = ken_block[l + 1];
					}
					ken_block.pop_back();
				}
			}
			if (is_first){
				wins++;
				for (int l = 0; l < ken_block.size() - 1; l++){
					ken_block[l] = ken_block[l + 1];
				}
				ken_block.pop_back();
			}/*
			for (int j = 0; j < ken_block.size(); j++){
				cout << ken_block[j] << " ";
			}
			cout << endl;
			system("PAUSE");*/
		}
		naomi_block = ken_1;
		ken_block = naomi_1;


		int wins1 = 0;
		for (int j = 0; j < N; j++){
			bool is_first = true;
			for (int k = 0; k < ken_block.size(); k++){
				if (is_first && ken_block[k] > naomi_block[j]){
					is_first = false;
					for (int l = k; l < ken_block.size() - 1; l++){
						ken_block[l] = ken_block[l + 1];
					}
					ken_block.pop_back();
				}
			}
			if (is_first){
				wins1++;
				for (int l = 0; l < ken_block.size() - 1; l++){
					ken_block[l] = ken_block[l + 1];
				}
				ken_block.pop_back();
			}
		}


		fout << "Case #" << i + 1 << ": " << N - wins1 << " " << wins << endl;
	}

	fin.close();
	fout.close();
	return 0;
}