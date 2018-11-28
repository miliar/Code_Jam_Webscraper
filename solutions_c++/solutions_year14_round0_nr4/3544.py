#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	int cases;
	int numbers;
	int i,j,k;
	int result_1, result_2;
	float tmp;
	vector<float> naomi, ken;

	fin >> cases;
	for(i = 0; i < cases; ++i) {
		naomi.clear();
		ken.clear();
		fin >> numbers;
		for(j = 0; j < numbers; ++j) {
			fin >> tmp;
			naomi.push_back(tmp);
		}
		for(j = 0; j < numbers; ++j) {
			fin >> tmp;
			ken.push_back(tmp);
		}
		sort(naomi.begin(), naomi.begin()+numbers);
		sort(ken.begin(), ken.begin()+numbers);
		k = 0;
		for(j = 0; j < numbers; ++j) {
			for(;naomi[j] > ken[k]; ++k) {
				if(k==numbers-1) break;
			}
			if(k==numbers-1) break;
			++k;
		}
		result_1 = numbers-j-1;
		if(naomi[j]>ken[k]) result_1++; 

		k = 0;
		for(j = 0; j < numbers; ++j) {
			for(;ken[j] > naomi[k]; ++k) {
				if(k==numbers-1) break;
			}
			if(k==numbers-1) break;
			++k;
		}
		result_2 = j+1;
		if(ken[j]>naomi[k]) result_2--;

		fout << "Case #" << i+1 << ": " << result_2 << " " << result_1 << endl;
	}
	fin.close();
	fout.close();
}